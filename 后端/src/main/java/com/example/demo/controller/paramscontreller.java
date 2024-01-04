package com.example.demo.controller;
import com.example.demo.entity.User;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class paramscontreller {
    @RequestMapping(value="/postTest1",method = RequestMethod.POST)
    public String postTest1(String username ,String password)
    {
        System.out.println("username="+username);
        System.out.println("password="+password);
        return "POST请求";
    }

    @RequestMapping(value="postTest2",method = RequestMethod.POST)
    public String postTest2(User user)
    {
        System.out.println(user);
        return "POST请求";
    }
    @RequestMapping(value="/postTest3",method = RequestMethod.POST)
    public String postTest3(@RequestBody User user)
    {
        System.out.println(user);
        return "POST请求";
    }
}
