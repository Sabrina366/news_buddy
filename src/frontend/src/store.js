import { createStore } from "vuex" 

const store = createStore({
   state:{
      articles:[
         {id:1, title: "spännande artikel", text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut erat dolor, placerat a aliquam eget, viverra id ante. Quisque sagittis blandit aliquam. Aenean nec dapibus mauris, nec laoreet felis. Aliquam purus nibh, molestie faucibus mollis eu, viverra ac turpis. Mauris at odio vulputate ligula cursus fermentum id sed ipsum. Morbi nec scelerisque est. Integer viverra ante ut vulputate tincidunt. Sed et dapibus metus, sed finibus ex. Nunc a scelerisque eros. Aenean vehicula vehicula sem quis pellentesque. Sed eleifend placerat efficitur. Duis eleifend elit ullamcorper, commodo lorem quis, viverra sem. Etiam tristique vitae velit vitae suscipit. Maecenas ut dolor a est sodales malesuada. Sed diam lacus, luctus ullamcorper tincidunt lacinia, finibus sed ipsum. Cras faucibus convallis nunc in dignissim.", author: "Gunilla"},
         {id:2, title: "extra extra", text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut erat dolor, placerat a aliquam eget, viverra id ante. Quisque sagittis blandit aliquam. Aenean nec dapibus mauris, nec laoreet felis. Aliquam purus nibh, molestie faucibus mollis eu, viverra ac turpis. Mauris at odio vulputate ligula cursus fermentum id sed ipsum. Morbi nec scelerisque est. Integer viverra ante ut vulputate tincidunt. Sed et dapibus metus, sed finibus ex. Nunc a scelerisque eros. Aenean vehicula vehicula sem quis pellentesque. Sed eleifend placerat efficitur. Duis eleifend elit ullamcorper, commodo lorem quis, viverra sem. Etiam tristique vitae velit vitae suscipit. Maecenas ut dolor a est sodales malesuada. Sed diam lacus, luctus ullamcorper tincidunt lacinia, finibus sed ipsum. Cras faucibus convallis nunc in dignissim.", author: "Sven"},
         {id:3, title: "Ointressant", text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut erat dolor, placerat a aliquam eget, viverra id ante. Quisque sagittis blandit aliquam. Aenean nec dapibus mauris, nec laoreet felis. Aliquam purus nibh, molestie faucibus mollis eu, viverra ac turpis. Mauris at odio vulputate ligula cursus fermentum id sed ipsum. Morbi nec scelerisque est. Integer viverra ante ut vulputate tincidunt. Sed et dapibus metus, sed finibus ex. Nunc a scelerisque eros. Aenean vehicula vehicula sem quis pellentesque. Sed eleifend placerat efficitur. Duis eleifend elit ullamcorper, commodo lorem quis, viverra sem. Etiam tristique vitae velit vitae suscipit. Maecenas ut dolor a est sodales malesuada. Sed diam lacus, luctus ullamcorper tincidunt lacinia, finibus sed ipsum. Cras faucibus convallis nunc in dignissim.", author: "Olle"}
       ]
   },
   mutations:{
    
   },
   actions:{
        
   }
})

export default store