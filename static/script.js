const navShow = () => {
  const burger = document.querySelector('.burger');
  const nav = document.querySelector('.nav-links');
  const links = document.querySelector('.nav-links li');

  
  burger.addEventListener('click',()=>{
    nav.classList.toggle('nav-active')

    links.forEach((link)=>{
      if (link.style.animation) {
        link.style.animation = '';
        }else{
          link.style.animation = "linksFade 0.5 ease forwards ${index / 5 + 0.2}s";
        }
    });

    burger.classList.toggle('close');

  });
}

navShow()