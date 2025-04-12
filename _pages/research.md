---
layout: archive
title: "Research"
permalink: /research/
---

<div class="research-container">
  <div class="research-header">
    <h1>Strong-Field Quantum Dynamics</h1>
    <p class="research-subtitle">Theoretical investigations of light-matter interactions in extreme conditions</p>
  </div>

  <div class="intro-section">
    <p>My research develops theoretical frameworks to understand how atoms and molecules behave in ultra-intense laser fields (10<sup>14</sup>-10<sup>18</sup> W/cm<sup>2</sup>). By combining analytical strong-field approximations with numerical solutions to the time-dependent Schrödinger equation, I explore phenomena where traditional perturbation theory breaks down.</p>
  </div>

  <div class="research-theme">
    <div class="theme-content">
      <h2>Strong-Field Ionization Dynamics</h2>
      <div class="theme-text">
        <p>When atoms interact with intense laser pulses, electrons can absorb many more photons than required for ionization, creating complex interference patterns in their momentum distributions.</p>
        
        <h3>Key Investigations:</h3>
        <ul>
          <li><strong>Quantum Trajectory Interference:</strong> Developed models explaining holographic patterns in photoelectron spectra through interfering ionization pathways</li>
          <li><strong>Non-Dipole Effects:</strong> Formulated corrections to the strong-field approximation accounting for magnetic field effects in high-intensity regimes</li>
          <li><strong>Carrier-Envelope Phase Control:</strong> Demonstrated how sub-cycle pulse structure determines electron emission directionality</li>
        </ul>
        
        <p>My work on generalized strong-field approximations has provided new tools for interpreting attosecond-scale electron dynamics.</p>
      </div>
      <div class="theme-image">
        <img src="/assets/img/pmd.png" alt="Photoelectron Momentum Distribution"/>
        <p class="img-caption">Calculated photoelectron momentum distribution showing characteristic interference structures</p>
      </div>
    </div>
  </div>

  <div class="research-theme">
    <div class="theme-content">
      <h2>Saddle-Point Methods in Strong-Field Physics</h2>
      <div class="theme-text">
        <p>The saddle-point approximation provides deep physical insight by revealing dominant quantum paths in complex time.</p>
        
        <h3>Methodological Advances:</h3>
        <ul>
          <li><strong>Complex-Time Dynamics:</strong> Extended standard approaches to include non-adiabatic effects in tunneling ionization</li>
          <li><strong>Interference Conditions:</strong> Derived phase-matching conditions explaining spectral oscillations in ATI spectra</li>
          <li><strong>Attosecond Resolution:</strong> Developed visualization techniques for sub-cycle electron dynamics</li>
        </ul>
        
        <p>These techniques have enabled more efficient calculations while maintaining physical interpretability.</p>
      </div>
      <div class="theme-image">
        <img src="/assets/img/saddlepoint.png" alt="Saddle Point Analysis"/>
        <p class="img-caption">Dominant quantum trajectories in complex time plane for different final momenta</p>
      </div>
    </div>
  </div>

  <div class="research-theme">
    <div class="theme-content">
      <h2>Twisted Light-Matter Interactions</h2>
      <div class="theme-text">
        <p>Vortex laser beams carrying orbital angular momentum create novel ionization dynamics with unique symmetry properties.</p>
        
        <h3>Findings:</h3>
        <ul>
          <li><strong>OAM Transfer Mechanisms:</strong> Identified selection rules governing angular momentum transfer to photoelectrons</li>
          <li><strong>Spatio-Temporal Coupling:</strong> Characterized how pulse vorticity affects sub-cycle ionization dynamics</li>
          <li><strong>Experimental Collaborations:</strong> Worked with experimental groups to verify theoretical predictions</li>
        </ul>
        
        <p>This research opens new possibilities for controlling electron wavepackets with structured light.</p>
      </div>
      <div class="theme-image">
        <img src="/assets/img/pulse.png" alt="Twisted Laser Pulse"/>
        <p class="img-caption">Spatial profile of a twisted laser pulse with topological charge l=2</p>
      </div>
    </div>
  </div>

  <div class="current-projects">
    <h2>Current Research Directions</h2>
    <div class="project-grid">
      <div class="project-card">
        <h3>Few-Cycle Vortex Pulses</h3>
        <p>Investigating how extreme bandwidth affects orbital angular momentum transfer during ionization</p>
      </div>
      <div class="project-card">
        <h3>Relativistic Corrections</h3>
        <p>Developing models that include both magnetic field and relativistic mass shift effects</p>
      </div>
      <div class="project-card">
        <h3>Computational Methods</h3>
        <p>Implementing efficient numerical techniques for solving strong-field problems</p>
      </div>
    </div>
  </div>

  <div class="collaboration">
    <p>I welcome discussions about my research and potential collaborations. <a href="/contact/">Contact me</a> if you're interested in these topics or have related questions.</p>
  </div>
</div>

<style>
.research-container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 2rem;
  font-family: 'Helvetica Neue', Arial, sans-serif;
  color: #333;
  line-height: 1.6;
}

.research-header {
  text-align: center;
  margin-bottom: 2.5rem;
  padding-bottom: 1rem;
}

.research-header h1 {
  font-size: 2.4rem;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.research-subtitle {
  font-size: 1.2rem;
  color: #7f8c8d;
  font-weight: 300;
}

.intro-section {
  margin-bottom: 3rem;
  font-size: 1.1rem;
  text-align: justify;
  padding: 0 1rem;
}

.research-theme {
  margin-bottom: 3.5rem;
}

.theme-content {
  display: flex;
  gap: 2rem;
  align-items: flex-start;
}

.theme-text {
  flex: 1.5;
}

.theme-image {
  flex: 1;
  min-width: 300px;
  margin-top: 0.5rem;
}

.theme-image img {
  width: 100%;
  border-radius: 6px;
  box-shadow: 0 5px 20px rgba(0,0,0,0.08);
  transition: transform 0.3s ease;
}

.theme-image img:hover {
  transform: scale(1.02);
}

.img-caption {
  font-size: 0.85rem;
  color: #666;
  text-align: center;
  margin-top: 0.5rem;
}

h2 {
  color: #2980b9;
  font-size: 1.6rem;
  margin-top: 2rem;
  margin-bottom: 1rem;
  padding-bottom: 0.3rem;
  border-bottom: 1px solid #eee;
}

h3 {
  color: #3498db;
  font-size: 1.2rem;
  margin-top: 1.2rem;
  margin-bottom: 0.5rem;
}

ul {
  padding-left: 1.3rem;
}

li {
  margin-bottom: 0.6rem;
}

.current-projects {
  margin: 4rem 0;
}

.project-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-top: 1.5rem;
}

.project-card {
  background: #f8f9fa;
  padding: 1.3rem;
  border-radius: 6px;
  border-left: 3px solid #3498db;
}

.project-card h3 {
  margin-top: 0;
}

.collaboration {
  margin-top: 3rem;
  padding: 1.5rem;
  text-align: center;
  background: #f0f7fc;
  border-radius: 6px;
  font-size: 1.05rem;
}

.collaboration a {
  color: #2980b9;
  font-weight: 500;
  text-decoration: none;
}

.collaboration a:hover {
  text-decoration: underline;
}

@media (max-width: 768px) {
  .theme-content {
    flex-direction: column;
  }
  
  .theme-image {
    margin-top: 1.5rem;
    width: 100%;
  }
  
  .project-grid {
    grid-template-columns: 1fr;
  }
}
</style>
