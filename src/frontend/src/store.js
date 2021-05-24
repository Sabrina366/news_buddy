import { createStore } from "vuex" 

const store = createStore({
   state:{
      articles:[
         {id:1, title: "spännande artikel", text: "blalbalbla", author: "Gunilla"},
         {id:2, title: "extra extra", text: "blablalbal", author: "Sven"},
         {id:3, title: "Ointressant", text: "blablablalb", author: "Olle"}
       ]
   },
   mutations:{
    
   },
   actions:{
        
   }
})

export default store