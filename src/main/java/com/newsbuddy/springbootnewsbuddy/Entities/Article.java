package com.newsbuddy.springbootnewsbuddy.Entities;


import javax.persistence.*;

@Entity
@Table(name = "articles")
public class Article {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;
    private String title;
    private String author;
    private String pub_date;
    private String url;
    private String text;
    private String timestamp;
    private String summary;
    private float score;


    public Article() {
    }

    public Article(String title, String author, String pub_date, String url, String text, String timestamp) {
        this.title = title;
        this.author = author;
        this.pub_date = pub_date;
        this.url = url;
        this.text = text;
        this.timestamp = timestamp;
    }

    public Article(int id, String title, String author, String pub_date, String url, String text, String timestamp, String summary, float score) {
        this.id = id;
        this.title = title;
        this.author = author;
        this.pub_date = pub_date;
        this.url = url;
        this.text = text;
        this.timestamp = timestamp;
        this.summary = summary;
        this.score = score;
    }

    public String getSummary() {
        return summary;
    }

    public void setSummary(String summary) {
        this.summary = summary;
    }

    public float getScore() {
        return score;
    }

    public void setScore(float score) {
        this.score = score;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public String getpub_date() {
        return pub_date;
    }

    public void setpub_date(String pub_date) {
        this.pub_date = pub_date;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }

    @Override
    public String toString() {
        return "Article{" +
                "id=" + id +
                ", title='" + title + '\'' +
                ", author='" + author + '\'' +
                ", pub_date='" + pub_date + '\'' +
                ", url='" + url + '\'' +
                ", text='" + text + '\'' +
                ", timestamp='" + timestamp + '\'' +
                ", summary='" + summary + '\'' +
                ", score=" + score +
                '}';
    }

}