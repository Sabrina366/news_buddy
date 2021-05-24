package com.newsbuddy.springbootnewsbuddy.Repositories;

import com.newsbuddy.springbootnewsbuddy.Entities.User;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface UserRepository extends CrudRepository<User, Integer> {

    public User findByUsername(String name);
}
