<template>
    <div id="contact">
        <div>
            <h1>Love to hear from you</h1>
            <h1>Get in touch 👋🏼</h1>
        </div>
        <div class="container">
            <form name="submit-to-google-sheet">
                <input type="text" name="First-Name" placeholder="First name" required>
                <input type="text" name="Last-Name" placeholder="Last Name" required>
                <input type="email" name="Email" placeholder="E-mail adress" required>
                <input type="text" name="Number" placeholder="Phone number" required>
                <textarea name="Message" rows="3" placeholder="Your message"></textarea>
                <button type="submit" class="btn">Submit</button>
            </form>
            <span id="msg"></span>
        </div>
    </div>
</template>

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

form .btn {
    border: none;
    background-color: #8E2DE2;
    color: white;
    padding: 20px 80px;
    border-radius: 10px;
    font-size: 16px;
    margin-top: 4%;
    margin-left: 35%;
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

<script>
export default {
    name: 'about',
    data() {
        return {
        }
    },
}
</script>