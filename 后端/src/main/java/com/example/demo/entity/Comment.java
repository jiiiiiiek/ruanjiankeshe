package com.example.demo.entity;

public class Comment {
    private String commid;
    private String commgender;
    private String commip;
    private String commtime;
    private String commcontent;

    private double touch;
    private double surprise;
    private double amusement;
    private double sadness;
    private double curiosity;
    private double anger;

    public String getCommid() {
        return commid;
    }

    public void setCommid(String commid) {
        this.commid = commid;
    }

    public String getCommgender() {
        return commgender;
    }

    public void setCommgender(String commgender) {
        this.commgender = commgender;
    }

    public String getCommip() {
        return commip;
    }

    public void setCommip(String commip) {
        this.commip = commip;
    }

    public String getCommtime() {
        return commtime;
    }

    public void setCommtime(String commtime) {
        this.commtime = commtime;
    }

    public String getCommcontent() {
        return commcontent;
    }

    public void setCommcontent(String commcontent) {
        this.commcontent = commcontent;
    }

    public double getTouch() {
        return touch;
    }

    public void setTouch(double touch) {
        this.touch = touch;
    }

    public double getSurprise() {
        return surprise;
    }

    public void setSurprise(double surprise) {
        this.surprise = surprise;
    }

    public double getAmusement() {
        return amusement;
    }

    public void setAmusement(double amusement) {
        this.amusement = amusement;
    }

    public double getSadness() {
        return sadness;
    }

    public void setSadness(double sadness) {
        this.sadness = sadness;
    }

    public double getCuriosity() {
        return curiosity;
    }

    public void setCuriosity(double curiosity) {
        this.curiosity = curiosity;
    }

    public double getAnger() {
        return anger;
    }

    public void setAnger(double anger) {
        this.anger = anger;
    }

    @Override
    public String toString() {
        return "Comment{" +
                "commid='" + commid + '\'' +
                ", commgender='" + commgender + '\'' +
                ", commip='" + commip + '\'' +
                ", commtime='" + commtime + '\'' +
                ", commcontent='" + commcontent + '\'' +
                ", touch=" + touch +
                ", surprise=" + surprise +
                ", amusement=" + amusement +
                ", sadness=" + sadness +
                ", curiosity=" + curiosity +
                ", anger=" + anger +
                '}';
    }
}