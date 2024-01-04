package com.example.demo.mapper;

import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.example.demo.entity.Comment;
import com.example.demo.entity.video;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Map;

@Repository
public interface comMapper {
    @Select("select * from video")//查询视频信息
    List<video> getvideoinfo();
    @Select("select count(*) from comment")//获取评论条数
    int getcommcount();
    @Select("select * from comment")//按页查询评论
    Page<Comment> selectPage(IPage<Comment> page);
    @Select("select AVG(touch) from comment")//计算感动情感指数的平均值
    List<Map<String, Object>> getavertouch();
    @Select("select AVG(surprise) from comment")//计算感动情感指数的平均值
    List<Map<String, Object>> getaversurprise();
    @Select("select AVG(amusement) from comment")//计算感动情感指数的平均值
    List<Map<String, Object>> getaveramusement();
    @Select("select AVG(sadness) from comment")//计算感动情感指数的平均值
    List<Map<String, Object>> getaversadness();
    @Select("select AVG(curiosity) from comment")//计算感动情感指数的平均值
    List<Map<String, Object>> getavercuriosity();
    @Select("select AVG(anger) from comment")//计算感动情感指数的平均值
    List<Map<String, Object>> getaveranger();
    @Select("select commgender,count(*) as gendercount from comment group by commgender order by gendercount desc limit 3")//计算性别出现次数
    List<Map<String,Object>> countgender();
    @Select("select commip,count(*) as ipcount from comment group by commip order by ipcount desc limit 10")//查询ip列的出现前十次数
    List<Map<String,Object>> countip();
}
