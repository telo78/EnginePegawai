<template>
  <footer class="w-100 py-4 flex-shrink-0 mt-5 text-left">
    <div class="container py-4">
      <div class="row gy-4 gx-5">
        <div class="col-lg-4 col-md-6">
          <h5 class="h1 text-white">Playbook</h5>
          <p class="small text-muted">
            Playbook adalah platform untuk mencari berbagai kursus online dalam
            satu wadah yang interaktif
          </p>
          <p class="small text-muted mb-0">
            &copy; Copyrights. All rights reserved.
            <a class="text-primary" href="https://ppkasn.setneg.go.id/"
              >PPKASN Kemensetneg</a
            >
          </p>
        </div>
        <div class="col-lg-2 col-md-6">
          <h5 class="text-white mb-3">Quick links</h5>
          <ul class="list-unstyled text-muted">
            <li><a href="/">Home</a></li>
            <li><a href="/course">Course</a></li>
            <li><a href="#">FAQ</a></li>
          </ul>
        </div>
        <div class="col-lg-4 col-md-6">
          <h5 class="text-white mb-3">Social Media</h5>
          <div class="row container d-flex justify-content-between">
            <div class="col-md-12">
              <a
                href="#"
                class="btn btn-primary btn-rounded btn-icon mr-2 mb-2"
                id="socialLink"
              >
                <i class="fa fa-facebook"></i>
              </a>
              <a
                href="#"
                class="btn btn-dark btn-rounded btn-icon mr-2 mb-2"
                id="socialLink"
              >
                <i class="fa fa-instagram"></i>
              </a>
              <a
                href="#"
                class="btn btn-danger btn-rounded btn-icon mr-2 mb-2"
                id="socialLink"
              >
                <i class="fa fa-youtube"></i>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<style scoped>
#socialLink {
  color: white;
}
footer {
  background: #212529;
}
.text-small {
  font-size: 0.9rem;
}

a {
  color: inherit;
  text-decoration: none;
  transition: all 0.3s;
}

a:hover,
a:focus {
  text-decoration: none;
}

.form-control {
  background: #212529;
  border-color: #545454;
}

.form-control:focus {
  background: #212529;
}
</style>

<script>
export default {
  name: "Footer",
};
</script>
