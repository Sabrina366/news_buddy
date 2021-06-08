package com.newsbuddy.springbootnewsbuddy.Controllers;

import com.newsbuddy.springbootnewsbuddy.Entities.Article;
import com.newsbuddy.springbootnewsbuddy.Services.ArticleService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
public class ArticleController {

    @Autowired
    ArticleService articleService;

    @GetMapping("/spring/api/articles/{id}")
    public Optional<Article> getArticleById(@PathVariable int id){
        return articleService.getArticleById(id);
    }

    @GetMapping("/rest/spring/api/articles")
    public List<Article> getAllArticles() {
        return articleService.getAllArticles();
    }

    @PostMapping("/rest/spring/api/articles")
    public Article addNewArticle(@RequestBody Article article){
        return articleService.addArticle(article);
    }

    @DeleteMapping("/rest/spring/api/articles/{id}")
    public void deleteById(@PathVariable int id){
        articleService.deleteById(id);
    }

    @GetMapping("api/sanic/articles")
    public Article[] getArticlesFromSanic(){
        return articleService.getArticlesFromSanic();
    }

    @PostMapping("api/sanic/articles")
    public Article postArticleToSanic(@RequestBody Article article){
        return articleService.postArticleToSanic(article);
    }

    @DeleteMapping("api/sanic/articles/{id}")
    public void deleteSanicArticle(@PathVariable int id){
        articleService.deleteFromSanic(id);
    }
}
