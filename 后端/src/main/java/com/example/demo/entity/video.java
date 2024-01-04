package com.example.demo.entity;

public class video {
    private String videotitle;
    private String videotime;
    private int videoview;
    private int videolike;
    private int videocoin;
    private int videofavorite;
    private int videoshare;

    @Override
    public String toString() {
        return "video{" +
                "videotitle='" + videotitle + '\'' +
                ", videotime='" + videotime + '\'' +
                ", videoview=" + videoview +
                ", videolike=" + videolike +
                ", videocoin=" + videocoin +
                ", videofavorite=" + videofavorite +
                ", videoshare=" + videoshare +
                '}';
    }

    public String getVideotitle() {
        return videotitle;
    }

    public void setVideotitle(String videotitle) {
        this.videotitle = videotitle;
    }

    public String getVideotime() {
        return videotime;
    }

    public void setVideotime(String videotime) {
        this.videotime = videotime;
    }

    public int getVideoview() {
        return videoview;
    }

    public void setVideoview(int videoview) {
        this.videoview = videoview;
    }

    public int getVideolike() {
        return videolike;
    }

    public void setVideolike(int videolike) {
        this.videolike = videolike;
    }

    public int getVideocoin() {
        return videocoin;
    }

    public void setVideocoin(int videocoin) {
        this.videocoin = videocoin;
    }

    public int getVideofavorite() {
        return videofavorite;
    }

    public void setVideofavorite(int videofavorite) {
        this.videofavorite = videofavorite;
    }

    public int getVideoshare() {
        return videoshare;
    }

    public void setVideoshare(int videoshare) {
        this.videoshare = videoshare;
    }
}
