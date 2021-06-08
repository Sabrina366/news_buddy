package com.newsbuddy.springbootnewsbuddy.Controllers;

import com.newsbuddy.springbootnewsbuddy.Entities.User;
import com.newsbuddy.springbootnewsbuddy.Services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class UserController {

    @Autowired
    UserService userService;


    @PostMapping("/api/register")
    public User register(@RequestBody User user){
        return userService.register(user);
    }

    @GetMapping("/spring/api/users")
    public List<User> getUsers(){
        return userService.getAllUsers();
    }

    @PostMapping("/spring/api/users")
    public User addNewUser(@RequestBody User user){
        return userService.addUser(user);
    }

    @GetMapping("api/sanic/users")
    public User[] getUsersFromSanic(){
        return userService.getUsersFromSanic();
    }

    @PostMapping("api/sanic/users")
    public User postUserToSanic(@RequestBody User user){
        return userService.postUserToSanic(user);
    }

    @DeleteMapping("api/sanic/users/{id}")
    public void deleteSanicUser(@PathVariable int id){
        userService.deleteFromSanic(id);
    }

}