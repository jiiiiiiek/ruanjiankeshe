package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Webcontroller {
    @GetMapping("/hello")
    public String Hello(String nickname,String password)
    {
        System.out.println(password);
        return "你好" + nickname;
    }
}
