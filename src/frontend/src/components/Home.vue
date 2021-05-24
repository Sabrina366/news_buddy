<template>
    <div class="homepage">
        <a href="/">
            <img alt="Vue logo" src="../assets/temp-frontpage-hero.png" />
        </a>
        <form action="">
            <textarea v-model="message" placeholder="search for content..."></textarea>
            <button>Search</button>
        </form>
        <div class="articles">
            <article>
                <h2>Title</h2>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Neque iure quis cum soluta corrupti sit vel, possimus facere sequi provident nesciunt, porro rem ex in dolorum rerum exercitationem omnis laboriosam!
                </p>
            </article>
            <article>
                <h2>Title</h2>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Neque iure quis cum soluta corrupti sit vel, possimus facere sequi provident nesciunt, porro rem ex in dolorum rerum exercitationem omnis laboriosam!
                </p>
            </article>
            <article>
                <h2>Title</h2>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Neque iure quis cum soluta corrupti sit vel, possimus facere sequi provident nesciunt, porro rem ex in dolorum rerum exercitationem omnis laboriosam!
                </p>
            </article>
            <article>
                <h2>Title</h2>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Neque iure quis cum soluta corrupti sit vel, possimus facere sequi provident nesciunt, porro rem ex in dolorum rerum exercitationem omnis laboriosam!
                </p>
            </article>
            <article>
                <h2>Title</h2>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Neque iure quis cum soluta corrupti sit vel, possimus facere sequi provident nesciunt, porro rem ex in dolorum rerum exercitationem omnis laboriosam!
                </p>
            </article>
            <article>
                <h2>Title</h2>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Neque iure quis cum soluta corrupti sit vel, possimus facere sequi provident nesciunt, porro rem ex in dolorum rerum exercitationem omnis laboriosam!
                </p>
            </article>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.homepage {
    display: flex;
    flex-direction: column;
    align-items: center;
}

img {
    padding: 40px;
}

form {
    display: flex;
    flex-direction: column;
    width: 80%;
    max-width: 800px;
    height: 200px;
}

textarea {
    height: 120px;
    border: 3px solid #5474AA;
    padding: 5px;
    margin: 5px;
    resize: none;
    border-radius: 4px;
}

button {
    display: flex;
    align-self: flex-end;
    background-color: #DDEFFD;
    color: #5474AA;
    border-radius: 4px;
    border: none;
    padding: 5px;
    margin: 5px;
    font-weight: 600;
}

.articles{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

article {
    width: 300px;
    border: dashed 2px rgb(196, 186, 186);
    margin: 40px;
    padding: 10px;
    border-radius: 4px;
}

</style>