package com.newsbuddy.springbootnewsbuddy.Repositories;

import com.newsbuddy.springbootnewsbuddy.Entities.Article;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ArticleRepository extends CrudRepository<Article, Integer> {

    public Article findByTitle(String title);

    public List<Article> findAllByTitleIgnoreCase(String title);

}