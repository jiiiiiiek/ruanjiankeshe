package com.example.demo.controller;

import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.example.demo.entity.Comment;
import com.example.demo.entity.Url;
import com.example.demo.entity.content;
import com.example.demo.entity.video;
import com.example.demo.mapper.Anamapper;
import com.example.demo.mapper.PaChongMapper;
import com.example.demo.mapper.comMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@CrossOrigin
public class comcontroller {
    @Autowired
    private comMapper ComMapper;
    @Autowired
    private PaChongMapper paChongMapper;
    @Autowired
    private Anamapper anamapper;

    @PostMapping(value="/AnaContent")//分析单独的一句话
    public List<Map<String, String>> anacontent(@RequestBody content Content)
    {
        List<Map<String, String>> motionlist=anamapper.executeana(Content.getContent());
        return motionlist;
    }
    //爬虫爬取B站评论,并返回前20条评论
    @RequestMapping(value="/PaChong",method = RequestMethod.POST)
    public List<Object> pachong(@RequestBody Url url)
    {
        paChongMapper.executepython(url.getUrl());
        List<video> vinfo=ComMapper.getvideoinfo();
        Page<Comment> page=new Page<>(1,20);
        IPage iPage=ComMapper.selectPage(page);
        List<Object> mergelist=new ArrayList<>();
        mergelist.addAll(vinfo);
        mergelist.addAll(iPage.getRecords());
        return mergelist;
    }

    //分页查询 一页20条评论
    @PostMapping("/comm/findbypage")
    public List<Object> findbypage(int page0)
    {
        Page<Comment> page=new Page<>(page0,20);
        List<video> vinfo=ComMapper.getvideoinfo();
        IPage iPage=ComMapper.selectPage(page);
        List<Object> mergelist=new ArrayList<>();
        mergelist.addAll(vinfo);
        mergelist.addAll(iPage.getRecords());
        return mergelist;
    }
    @GetMapping("/comm/table")
    public List table()
    {
        List<Map<String, Object>> avertouch=ComMapper.getavertouch();
        List<Map<String, Object>> aversurprise=ComMapper.getaversurprise();
        List<Map<String, Object>> averamusement=ComMapper.getaveramusement();
        List<Map<String, Object>> aversadness=ComMapper.getaversadness();
        List<Map<String, Object>> avercuriosity=ComMapper.getavercuriosity();
        List<Map<String, Object>> averanger=ComMapper.getaveranger();
        List<Map<String, Object>> list1=new ArrayList<>();
        list1.addAll(avertouch);
        list1.addAll(aversurprise);
        list1.addAll(averamusement);
        list1.addAll(aversadness);
        list1.addAll(avercuriosity);
        list1.addAll(averanger);
        System.out.println(list1);

        List<Map<String,Object>> list2=ComMapper.countgender();
        System.out.println(list2);

        List<Map<String,Object>> list3=ComMapper.countip();
        int ccount=ComMapper.getcommcount();
        for(Map<String,Object>item:list3){
            int count=((Long)item.get("ipcount")).intValue();
            ccount-=count;
        }
        Map<String,Object>cip=new HashMap<>();
        cip.put("commip","其他");
        cip.put("ipcount",ccount);
        list3.add(cip);
        System.out.println(list3);

        List<Object> list=new ArrayList<>();
        list.addAll(list1);
        list.addAll(list2);
        list.addAll(list3);
        return list;
    }
}
