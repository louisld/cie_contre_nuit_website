import './main.scss';

// Fort Awesome
import { library, dom } from '@fortawesome/fontawesome-svg-core';
import { faSquareInstagram, faInstagram, faSquareGithub } from '@fortawesome/free-brands-svg-icons';
import { faEnvelope } from '@fortawesome/free-solid-svg-icons';

library.add(faSquareInstagram);
library.add(faInstagram);
library.add(faEnvelope);
library.add(faSquareGithub);

document.addEventListener('DOMContentLoaded', () => {

  // Fort Awesome watch
  dom.watch();

  // Navbar burger toggle
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
  $navbarBurgers.forEach( el => {
    el.addEventListener('click', () => {
      const target = el.dataset.target;
      const $target = document.getElementById(target);
      el.classList.toggle('is-active');
      $target.classList.toggle('is-active');
    });
  });
});