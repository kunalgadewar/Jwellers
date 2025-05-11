import React from 'react';
import Slider from 'react-slick';
import './Home.css';
import "slick-carousel/slick/slick.css"; 
import "slick-carousel/slick/slick-theme.css";

export default function Home() {
  const settings = {
    dots: true,
    infinite: true,
    speed: 300,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 3000
  };

  const slides = [
    {
      title: "Gold Jewellery",
      image: "https://m.media-amazon.com/images/I/511CPr6ebML._SY395_.jpg"
    },
    {
      title: "Silver Jewellery",
      image: "https://m.media-amazon.com/images/I/511CPr6ebML._SY395_.jpg"
    },
    {
      title: "Platinum Jewellery",
      image: "https://m.media-amazon.com/images/I/511CPr6ebML._SY395_.jpg"
    }
  ];

  return (
    <div>
    <div className="carousel-container">
      <Slider {...settings}>
        {slides.map((slide, index) => (
          <div key={index} className="carousel-slide">
            <div
              className="carousel-background"
              style={{ backgroundImage: `url(${slide.image})` }}
            >
              <div className="carousel-overlay">
                <h2>{slide.title}</h2>
              </div>
            </div>
          </div>
        ))}
      </Slider>
    </div>


    <div className="product-section">
  <h2 className="section-title">Our Jewellery Collection</h2>
  <div className="product-cards">
    <div className="product-card">
      <img src="https://m.media-amazon.com/images/I/511CPr6ebML._SY395_.jpg" alt="Gold" />
      <div className="card-info">
        <h3>Gold</h3>
        <p>₹5,600</p>
        <p>Per gram rate: ₹5,600</p>
      </div>
    </div>
    <div className="product-card">
      <img src="https://m.media-amazon.com/images/I/511CPr6ebML._SY395_.jpg" alt="Silver" />
      <div className="card-info">
        <h3>Silver</h3>
        <p>₹70</p>
        <p>Per gram rate: ₹70</p>
      </div>
    </div>
    <div className="product-card">
      <img src="https://m.media-amazon.com/images/I/511CPr6ebML._SY395_.jpg" alt="Platinum" />
      <div className="card-info">
        <h3>Platinum</h3>
        <p>₹3,200</p>
        <p>Per gram rate: ₹3,200</p>
      </div>
    </div>
  </div>
</div>

    </div>
  );
}
