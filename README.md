<div class="slider">
  <div class="slides">
    <div class="slide"><img src="https://file.hstatic.net/200000503583/file/anh-di-bien-chup-sau-lung-_15__a19a0d1be5bd4d8b8c27e4337ad488a3.jpg" alt="Image 1" width="800"></div>
    <div class="slide"><img src="https://file.hstatic.net/200000503583/file/anh-di-bien-chup-sau-lung-_15__a19a0d1be5bd4d8b8c27e4337ad488a3.jpg" alt="Image 2" width="800"></div>
    <div class="slide"><img src="https://file.hstatic.net/200000503583/file/anh-di-bien-chup-sau-lung-_15__a19a0d1be5bd4d8b8c27e4337ad488a3.jpg" alt ="Image 3" width="800"></div>
    <div class="slide"><img src="https://file.hstatic.net/200000503583/file/anh-di-bien-chup-sau-lung-_15__a19a0d1be5bd4d8b8c27e4337ad488a3.jpg" alt="Image 4" width="800"></div>
    <div class="slide"><img src="https://file.hstatic.net/200000503583/file/anh-di-bien-chup-sau-lung-_15__a19a0d1be5bd4d8b8c27e4337ad488a3.jpg" alt="Image 5" width="800"></div>
  </div>
  <button class="prev">❮</button>
  <button class="next">❯</button>
</div>

<style>
.slider {
  position: relative;
  max-width: 800px;
  margin: auto;
  overflow: hidden;
}

.slides {
  display: flex;
  transition: transform 0.5s ease;
}

.slide {
  min-width: 100%;
  transition: opacity 0.5s ease;
  opacity: 0;
}

.slide.active {
  opacity: 1;
}
</style>
