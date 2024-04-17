// script.js

document.getElementById('searchBtn').addEventListener('click', function() {
    var searchInput = document.getElementById('searchInput').value.toLowerCase();
    var products = document.querySelectorAll('.product');
  
    products.forEach(function(product) {
        var productName = product.querySelector('.product-name').textContent.toLowerCase();
        if (productName.includes(searchInput)) {
            product.style.display = 'block';
        } else {
            product.style.display = 'none';
        }
    });
  });
  


document.querySelectorAll('.read-more').forEach(function(element) {
    element.addEventListener('click', function() {
        var moreText = this.nextElementSibling;
        if (moreText.style.display === 'none' || moreText.style.display === '') {
            moreText.style.display = 'inline';
            this.textContent = 'Read Less';
        } else {
            moreText.style.display = 'none';
            this.textContent = 'Read More...';
        }
    });
});
