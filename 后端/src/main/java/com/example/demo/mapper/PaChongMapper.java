package com.example.demo.mapper;


import org.springframework.stereotype.Repository;

import java.io.*;
import java.util.stream.Collectors;

@Repository
public interface PaChongMapper {
    default public void executepython(String url)//输入url
    {
        try{
            //String url="https://www.bilibili.com/video/BV1Bu4y1w7cc/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=079901b9e6fa8d7726d21181e17a22b2";
            File f=new File("F:\\testweb\\demo\\src\\main\\resources\\python\\url.txt");
            BufferedWriter out =new BufferedWriter(new FileWriter(f));
            out.write(url);
            out.close();//通过写入url到文本文件中来传参
            ProcessBuilder pb=new ProcessBuilder("D:\\anaconda\\envs\\DL\\python.exe","F:\\testweb\\demo\\src\\main\\resources\\python\\BiliPaChong.py");
            Process proc=pb.start();
            BufferedReader in =new BufferedReader(new InputStreamReader(proc.getInputStream()));
            String errorOutput = new BufferedReader(new InputStreamReader(proc.getErrorStream())).lines().collect(Collectors.joining("\n"));
            String line;
            while((line=in.readLine())!=null){
                System.out.println(line);
            }
            in.close();
            int exitCode = proc.waitFor();
            System.out.println("Python脚本执行完毕,退出码：" + exitCode);
            System.out.println("Error output:\n" + errorOutput);
        }catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
