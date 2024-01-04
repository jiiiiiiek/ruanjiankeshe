package com.example.demo.mapper;

import org.springframework.stereotype.Repository;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@Repository
public interface Anamapper {
    default public List<Map<String, String>> executeana(String Content) {
        try {
            File f = new File("F:\\testweb\\demo\\src\\main\\resources\\python\\Content.txt");
            BufferedWriter out = new BufferedWriter(new FileWriter(f));
            out.write(Content);
            out.close();
            ProcessBuilder pb = new ProcessBuilder("D:\\anaconda\\envs\\DL\\python.exe", "F:\\testweb\\demo\\src\\main\\resources\\python\\anacont.py");
            Process proc = pb.start();
            String errorOutput = new BufferedReader(new InputStreamReader(proc.getErrorStream())).lines().collect(Collectors.joining("\n"));
            int exitCode = proc.waitFor();
            System.out.println("Python脚本执行完毕,退出码：" + exitCode);
            System.out.println("Error output:\n" + errorOutput);
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
        List<Map<String, String>> motionlist = new ArrayList<>();
        Map<String, String> touchkey = new HashMap<>();
        Map<String, String> surprisekey = new HashMap<>();
        Map<String, String> amusementkey = new HashMap<>();
        Map<String, String> sadnesskey = new HashMap<>();
        Map<String, String> curiositykey = new HashMap<>();
        Map<String, String> angerkey = new HashMap<>();
        File file = new File("F:\\testweb\\demo\\src\\main\\resources\\python\\motion.txt");
        List<String> lines=new ArrayList<>();
        try {
            BufferedReader br = new BufferedReader(new FileReader(file));
            String line=null;
            while((line = br.readLine())!=null){
                lines.add(line);
            }
            br.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
        String touch=lines.get(0);
        String surprise=lines.get(1);
        String amusement=lines.get(2);
        String sadness=lines.get(3);
        String curiosity=lines.get(4);
        String anger=lines.get(5);
        touchkey.put("touch",touch);
        surprisekey.put("surprise",surprise);
        amusementkey.put("amusement",amusement);
        sadnesskey.put("sadness",sadness);
        curiositykey.put("curiosity",curiosity);
        angerkey.put("anger",anger);
        motionlist.add(touchkey);
        motionlist.add(surprisekey);
        motionlist.add(amusementkey);
        motionlist.add(sadnesskey);
        motionlist.add(curiositykey);
        motionlist.add(angerkey);
        return motionlist;
    }
}
