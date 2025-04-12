---
layout: archive
title: "Research"
permalink: /research/
---

<div class="research-page">
  <header class="research-header">
    <h1>Strong-Field Quantum Dynamics</h1>
    <p class="research-subtitle">Theoretical investigations of light-matter interactions in intense laser fields</p>
  </header>

  <section class="intro-section">
    <p>My research develops theoretical frameworks to understand how atoms and molecules behave in ultra-intense laser fields (10<sup>13</sup>-10<sup>18</sup> W/cm<sup>2</sup>). By combining analytical strong-field approximations with numerical solutions to the time-dependent Schrödinger equation, I explore phenomena where traditional perturbation theory breaks down.</p>
  </section>

  <div class="research-theme">
    <div class="theme-description">
      <h2>Strong-Field Ionization Dynamics</h2>
      <p>When atoms interact with intense laser pulses, electrons can absorb many more photons than required for ionization, creating complex interference patterns in their momentum distributions.</p>
      
      <div class="research-details">
        <h3>Key Contributions:</h3>
        <ul>
          <li>Developed models explaining holographic patterns in photoelectron spectra through interfering ionization pathways</li>
          <li>Formulated corrections to the strong-field approximation accounting for magnetic field effects</li>
          <li>Demonstrated how sub-cycle pulse structure determines electron emission directionality</li>
        </ul>
      </div>
    </div>
    
    <figure class="theme-visual">
      <img src="/assets/img/pmd.png" alt="Photoelectron Momentum Distribution"/>
      <figcaption>Calculated photoelectron momentum distribution showing characteristic interference structures</figcaption>
    </figure>
  </div>

  <div class="research-theme reversed">
    <div class="theme-description">
      <h2>Saddle-Point Methods</h2>
      <p>The saddle-point approximation provides deep physical insight by revealing dominant quantum paths in complex time.</p>
      
      <div class="research-details">
        <h3>Methodological Advances:</h3>
        <ul>
          <li>Extended standard approaches to include non-adiabatic effects in tunneling ionization</li>
          <li>Derived phase-matching conditions explaining spectral oscillations in ATI spectra</li>
          <li>Developed visualization techniques for sub-cycle electron dynamics</li>
        </ul>
      </div>
    </div>
    
    <figure class="theme-visual">
      <img src="/assets/img/saddlepoint.png" alt="Saddle Point Analysis"/>
      <figcaption>Saddle points on complex time plane with deformed integration contour</figcaption>
    </figure>
  </div>

  <div class="research-theme">
    <div class="theme-description">
      <h2>Twisted Light Interactions</h2>
      <p>Vortex laser beams carrying orbital angular momentum create novel ionization dynamics with unique symmetry properties.</p>
      
      <div class="research-details">
        <h3>Research Findings:</h3>
        <ul>
          <li>Identified selection rules governing angular momentum transfer to photoelectrons</li>
          <li>Characterized how pulse vorticity affects sub-cycle ionization dynamics</li>
          <li>Theoretical predictions verified through experimental collaborations</li>
        </ul>
      </div>
    </div>
    
    <figure class="theme-visual">
      <img src="/assets/img/pulse.png" alt="Twisted Laser Pulse"/>
      <figcaption>Spatial profile of a few-cycle laser pulse</figcaption>
    </figure>
  </div>

  <section class="current-work">
    <h2>Ongoing Investigations</h2>
    <div class="project-showcase">
      <article class="project-card">
        <h3>Few-Cycle Vortex Pulses</h3>
        <p>Examining orbital angular momentum transfer with ultra-short pulses</p>
      </article>
      <article class="project-card">
        <h3>Relativistic Corrections</h3>
        <p>Developing models incorporating magnetic field and mass shift effects</p>
      </article>
      <article class="project-card">
        <h3>Computational Methods</h3>
        <p>Implementing efficient numerical techniques for strong-field problems</p>
      </article>
    </div>
  </section>

  <section class="collaboration-note">
    <p>I welcome discussions about my research and potential collaborations. <a href="mailto:danish.dar@uni-jena.de">Contact me</a> to explore these topics further.</p>
  </section>
</div>

<style>
.research-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 3rem;
  font-family: 'Helvetica Neue', Arial, sans-serif;
  color: #333;
  line-height: 1.7;
}

.research-header {
  text-align: center;
  margin-bottom: 3rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid #eaeaea;
}

.research-header h1 {
  font-size: 2.6rem;
  color: #222;
  margin-bottom: 0.8rem;
  font-weight: 600;
}

.research-subtitle {
  font-size: 1.3rem;
  color: #555;
  font-weight: 300;
}

.intro-section {
  margin: 0 auto 4rem;
  max-width: 800px;
  font-size: 1.1rem;
  text-align: center;
}

.research-theme {
  display: flex;
  gap: 3rem;
  margin-bottom: 5rem;
  align-items: center;
}

.reversed {
  flex-direction: row-reverse;
}

.theme-description {
  flex: 1;
  min-width: 50%;
}

.theme-visual {
  flex: 1;
  min-width: 40%;
  margin: 0;
}

.theme-visual img {
  width: 100%;
  border-radius: 8px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.08);
  border: 1px solid #eee;
}

figcaption {
  font-size: 0.9rem;
  color: #666;
  text-align: center;
  margin-top: 1rem;
  line-height: 1.5;
}

h2 {
  color: #2c5282;
  font-size: 1.8rem;
  margin-bottom: 1.5rem;
  font-weight: 500;
}

h3 {
  color: #4a5568;
  font-size: 1.3rem;
  margin: 2rem 0 1rem;
  font-weight: 500;
}

ul {
  padding-left: 1.5rem;
  margin: 1.5rem 0;
}

li {
  margin-bottom: 0.8rem;
  position: relative;
  padding-left: 1rem;
}

li:before {
  content: "•";
  position: absolute;
  left: 0;
  color: #4a5568;
}

.current-work {
  margin: 6rem 0 4rem;
  text-align: center;
}

.project-showcase {
  display: flex;
  gap: 2rem;
  margin-top: 3rem;
  justify-content: center;
  flex-wrap: wrap;
}

.project-card {
  flex: 1;
  min-width: 280px;
  max-width: 350px;
  padding: 2rem;
  background: #f8fafc;
  border-radius: 8px;
  border-top: 3px solid #4299e1;
  box-shadow: 0 5px 15px rgba(0,0,0,0.03);
  transition: transform 0.2s ease;
}

.project-card:hover {
  transform: translateY(-5px);
}

.project-card h3 {
  color: #2b6cb0;
  margin-top: 0;
}

.collaboration-note {
  max-width: 700px;
  margin: 5rem auto;
  padding: 2rem;
  text-align: center;
  background: #ebf8ff;
  border-radius: 8px;
  font-size: 1.1rem;
}

.collaboration-note a {
  color: #2b6cb0;
  font-weight: 500;
  text-decoration: none;
  border-bottom: 1px dotted currentColor;
}

@media (max-width: 900px) {
  .research-page {
    padding: 2rem;
  }
  
  .research-theme,
  .reversed {
    flex-direction: column;
    gap: 2rem;
  }
  
  .theme-visual {
    width: 100%;
    max-width: 600px;
    margin: 0 auto;
  }
  
  .project-card {
    min-width: 100%;
  }
}

@media (max-width: 600px) {
  .research-header h1 {
    font-size: 2rem;
  }
  
  .research-subtitle {
    font-size: 1.1rem;
  }
  
  h2 {
    font-size: 1.6rem;
  }
}
</style>
