package com.newsbuddy.springbootnewsbuddy.Services;

import com.newsbuddy.springbootnewsbuddy.Entities.User;
import com.newsbuddy.springbootnewsbuddy.Repositories.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.List;

@Service
public class UserService {


    @Autowired
    UserRepository userRepository;
    String url = "http://127.0.0.1:8000/sanic/api/users/";
    RestTemplate restTemplate = new RestTemplate();

    public List<User> getAllUsers(){
        return (List<User>) userRepository.findAll();
    }

    public User addUser(User user){
        userRepository.save(user);
        return user;
    }

    public User[] getUsersFromSanic(){
        return restTemplate.getForObject(url, User[].class);
    }

    public User postUserToSanic(User user){
        return restTemplate.postForObject(url, user, User.class);
    }

    public void deleteFromSanic(int id){
        restTemplate.delete(url + id);
    }
}
