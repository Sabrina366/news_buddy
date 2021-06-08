package com.newsbuddy.springbootnewsbuddy.Controllers;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

@Controller
public class LoginController {

    @GetMapping("/login")
    public String login(){
        return "login";
    }

}