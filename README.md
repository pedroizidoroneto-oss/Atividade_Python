let particles = [];

function setup() {
  createCanvas(windowWidth, windowHeight);
  // Define o modo de cor para HSB (Matiz, Saturação, Brilho) para cores vibrantes
  colorMode(HSB, 360, 100, 100, 100);
}

function draw() {
  // Fundo preto com rastro (transparência) para efeito de movimento
  background(0, 0, 0, 10);

  // Cria novas partículas quando o mouse se move
  if (mouseIsPressed || mouseX !== pmouseX) {
    let p = new Particle(mouseX, mouseY);
    particles.push(p);
  }

  // Atualiza e desenha as partículas
  for (let i = particles.length - 1; i >= 0; i--) {
    particles[i].update();
    particles[i].show();
    
    // Remove partículas muito pequenas para manter a performance
    if (particles[i].finished()) {
      particles.splice(i, 1);
    }
  }
}

class Particle {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.vx = random(-2, 2);
    this.vy = random(-2, 2);
    this.alpha = 100;
    this.size = random(10, 30);
    // A cor depende da posição X do mouse
    this.color = map(mouseX, 0, width, 0, 360);
  }

  finished() {
    return this.alpha < 0;
  }

  update() {
    this.x += this.vx;
    this.y += this.vy;
    this.alpha -= 1.5; // Desvanece aos poucos
    this.size *= 0.98;  // Encolhe aos poucos
  }

  show() {
    noStroke();
    fill(this.color, 80, 100, this.alpha);
    ellipse(this.x, this.y, this.size);
  }
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
}





