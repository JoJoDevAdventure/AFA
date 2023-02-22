<template>
  <div class="about">
      <div class="container py-5">
        <div class="row h-100 align-items-center py-5">
          <div class="col-lg-6">
            <h1 class="display-4">About us</h1>
            <p class="lead text-muted mb-0">At Air Force Artisans, we are passionate about sneakers, art, and the boundless possibilities that arise when the two are combined. Founded with a vision to revolutionize sneaker culture, our company is dedicated to creating custom Air Force Ones that are more than just shoes – they are wearable works of art.<br> <br>

Our team of skilled artisans brings together years of experience and a deep love for sneaker design. Each pair of Air Force Ones is meticulously handcrafted with attention to detail, ensuring that every stitch, color, and pattern comes together flawlessly to create a one-of-a-kind masterpiece.</p>
          </div>
          <div class="col-lg-6 d-none d-lg-block"><img src="https://bootstrapious.com/i/snippets/sn-about/illus.png"
              alt="" class="img-fluid"></div>
        </div>
      </div>

    <div class="py-5">
      <div class="container py-5">
        <div class="row mb-4">
          <div class="col-lg-5">
            <h2 class="display-4 font-weight-light">Our team</h2>
            <p class="font-italic text-muted">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
          </div>
        </div>

        <div class="row text-center">
          <!-- Team item-->
          <div class="col-xl-3 col-sm-6 mb-5">
            <div class="bg-dark rounded shadow-sm py-5 px-4"><img
                src="https://bootstrapious.com/i/snippets/sn-about/avatar-4.png" alt="" width="100"
                class="img-fluid rounded-circle mb-3 img-thumbnail shadow-sm">
              <h5 class="mb-0">Joseph Bouhlel</h5><span class="small text-uppercase text-muted">CEO - Founder</span>
              <ul class="social mb-0 list-inline mt-3">
                <li class="list-inline-item"><a href="#" class="social-link"><i class="fa fa-facebook-f"></i></a></li>
                <li class="list-inline-item"><a href="#" class="social-link"><i class="fa fa-twitter"></i></a></li>
                <li class="list-inline-item"><a href="#" class="social-link"><i class="fa fa-instagram"></i></a></li>
                <li class="list-inline-item"><a href="#" class="social-link"><i class="fa fa-linkedin"></i></a></li>
              </ul>
            </div>
          </div>
          <!-- End-->

        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
@import "~@fortawesome/fontawesome-free/css/all.css";

.about {
  background-color: #0E0F0A;
  color: white;
}

.social-link {
  width: 30px;
  height: 30px;
  border: 1px solid #ddd;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #666;
  border-radius: 50%;
  transition: all 0.3s;
  font-size: 0.9rem;
}

.social-link:hover,
.social-link:focus {
  background: #ddd;
  text-decoration: none;
  color: #555;
}
</style>