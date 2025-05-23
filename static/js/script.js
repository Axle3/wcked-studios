function openModal(index) {
    document.getElementById(`modal-${index}`).style.display = "block";
  }
  
  function closeModal(index) {
    document.getElementById(`modal-${index}`).style.display = "none";
  }
  
  function scrollGallery(direction) {
    const gallery = document.querySelector('.gallery');
    const scrollAmount = 320; // card width + gap
    
    if (direction === 'left') {
        gallery.scrollBy({
            left: -scrollAmount,
            behavior: 'smooth'
        });
    } else {
        gallery.scrollBy({
            left: scrollAmount,
            behavior: 'smooth'
        });
    }
}
  