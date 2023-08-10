<template>
    <div id="contact">
        <div>
            <h1>Love to hear from you</h1>
            <h1>Get in touch 👋🏼</h1>
        </div>

        <div class="container">
            <form @submit="Feedback">
                <input type="text" name="First-Name" placeholder="First name" v-model="name" required>
                <input type="text" name="Last-Name" placeholder="Last Name" v-model="family_name" required>
                <input type="email" name="Email" placeholder="E-mail adress" v-model="email" required>
                <input type="text" name="Number" placeholder="Phone number" v-model="phone" required>
                <textarea name="Message" rows="3" placeholder="Your message" v-model="message" required></textarea>
                <button class="btn">Submit</button>
            </form>
            <span id="msg"></span>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import HomeView from './HomeView.vue';

export default {

    data() {
        return {
            name: '',
            family_name: '',
            phone: '',
            email: '',
            message: '',
        };
    },
    mounted() {
        document.title = 'Contact | AFA'
    },
    methods: {

        openModal() {
            state.modal_demo.show()
        },

        closeModal() {
            state.modal_demo.hide()
        },


        async Feedback() {

            const data = {
                'name': this.name,
                'family_name': this.family_name,
                'phone': this.phone,
                'email': this.email,
                'message': this.message,
            }
            
            this.$store.commit('setIsLoading', true)
            await axios
                .post('/api/v1/contact/', data)
                .then(response => {
                    if (response.status == 201) {

                        const routes = [
  { path: '/', name: 'home', component: HomeView },
  // ... other routes
];

                        this.$store.commit('setIsLoading', false)
                        this.$router.push({ name: '../' });
                    }
                })
                .catch(error => {
                    this.$store.commit('setIsLoading', false)
                    this.error.push('something went wrong. Please try again')
                })




        }
    }
};
</script>

<style scoped>
h1 {
    color: white;
    font-size: 52px;
    text-align: center;
}

.container {
    justify-content: center;
    align-items: center;
    justify-items: center;
}

form {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    max-width: 70%;
    width: 100%;
    padding: 20px;
    align-content: center;
    margin-left: 170px;
    margin-top: 60px;
}

form input {
    background: #262626;
    padding: 15px;
    color: #fff;
    font-size: 18px;
    border-image: linear-gradient(to right, #9671F6, #FD6756) 1;
    width: 49%;
    height: 70px;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 5px;
}

form textarea {
    width: 100%;
    outline: none;
    background: #262626;
    padding: 15px;
    margin-top: 15px;
    color: #fff;
    font-size: 18px;
    border-radius: 8px;
    border-image: linear-gradient(to right, #9671F6, #FD6756) 1;
}

.btn {
    border: none;
    background-color: #8E2DE2;
    color: white;
    padding: 20px 80px;
    border-radius: 10px;
    font-size: 16px;
    margin-top: 4%;
    margin-left: 40%;
    cursor: pointer;
    border-image: linear-gradient(to right, #9671F6, #FD6756) 1;
}

@media only screen and (max-width: 600px) {
    h1 {
        color: white;
        font-size: 38px;
        margin-left: 10px;
    }

    .container {
        margin-left: 0%;
    }

    form {
        display: grid;
        flex-wrap: wrap;
        max-width: 100%;
        width: 100%;
        padding: 20px;
        align-content: center;
    }

    form input {
        background: #262626;
        padding: 15px;
        color: #fff;
        font-size: 18px;
        width: 100%;
        height: 60px;
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 5px;
    }

    form textarea {
        width: 100%;
        outline: none;
        background: #262626;
        padding: 15px;
        margin-top: 15px;
        color: #fff;
        font-size: 18px;
        border-radius: 8px;
    }

    form .btn {
        border: none;
        background-color: #8E2DE2;
        color: white;
        padding: 15px 80px;
        border-radius: 10px;
        font-size: 16px;
        margin-top: 4%;
        margin-left: 0%;
        cursor: pointer;
    }
}
</style>
