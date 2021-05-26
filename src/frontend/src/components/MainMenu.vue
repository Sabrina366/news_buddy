<template>

 <nav class="navbar">
    <div class="logo">
    <a href="/"><img class="icon" src="src/assets/NewsBuddy-logo.png" alt="Icon"></a>
    <a href="/"><img class="icon-small" src="src/assets/NewsBuddy-IconSmall.png" alt="IconSmall"></a>
   </div>
   <div class="tags">
    <a href="/">Create Content</a>
    <a href="/">Articles</a>
   </div>
  </nav>

</template>

<script>
export default {
}
</script>

<style scoped>
.navbar{
  position: fixed;
  font-size: 20px;
  margin-bottom: 5px;
  align-items: center;
  flex-direction: row;
  display: flex;
  height: 0px;
}
.icon-small{
  display: none;
  align-content: flex-start;
}
.tags{
  justify-content: flex-end;
  flex-direction: row-reverse;
  min-width: 100px;
  align-content: flex-end;
}

.logo{
  width: 15%;
  float: left;
  margin: 0px;
  flex-grow: 1;
}
.icon {
  padding: 15px;
  background-size: cover;
  width: 30%;
  margin-top: 15px;
  display: flex;
}

  
.navbar a{
  color: #5474AA;
  text-decoration: none;
  padding: 15px;
}

.navbar a:hover{
  color: #DDEFFD;
}

@media (max-width: 1300px) {
  .icon{
    display: none;
  }
  .icon-small{
    display: flex;
    margin: 0%;
  }
  .logo{
  padding: 10px;
}
}

@media (max-width: 1000px) {
  .navbar {
    font-size: 15px;
    flex-direction: row;
    align-items: center;
    display: flex;
    justify-content: space-between;
  }
}

</style>