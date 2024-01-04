package com.example.demo.entity;

public class content {
    private String Content;

    @Override
    public String toString() {
        return "content{" +
                "Content='" + Content + '\'' +
                '}';
    }

    public String getContent() {
        return Content;
    }

    public void setContent(String content) {
        Content = content;
    }
}
