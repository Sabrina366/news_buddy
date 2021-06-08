package com.newsbuddy.springbootnewsbuddy.Services;

import com.newsbuddy.springbootnewsbuddy.Entities.Article;
import com.newsbuddy.springbootnewsbuddy.Repositories.ArticleRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.List;
import java.util.Optional;

@Service
public class ArticleService {

    @Autowired
    ArticleRepository articleRepository;

    String url = "http://127.0.0.1:8000/sanic/api/articles/";
    RestTemplate restTemplate = new RestTemplate();

    public List<Article> getAllArticles() {
        return (List<Article>) articleRepository.findAll();
    }

    public Optional<Article> getArticleById(int id){
        return articleRepository.findById(id);
    }


    public Article addArticle(Article article){
        articleRepository.save(article);
        return article;
    }

    public void deleteById(int id){
        articleRepository.deleteById(id);
    }

    public Article[] getArticlesFromSanic(){
        return restTemplate.getForObject(url, Article[].class);
    }


    public Article postArticleToSanic(Article article){
        return restTemplate.postForObject(url, article, Article.class);
    }

    public void deleteFromSanic(int id){
        restTemplate.delete(url + id);
    }



}