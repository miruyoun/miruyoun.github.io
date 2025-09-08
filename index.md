---
layout: default
---

<style>
/* Custom CSS to override minimal theme and create Matt Chapman-style layout */
.wrapper {
    max-width: 1200px;
    margin: 0 auto;
    padding: 40px 20px;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    background-color: #f8f9fa;
}

.portfolio-container {
    display: grid;
    grid-template-columns: 300px 1fr;
    gap: 60px;
    margin-top: 20px;
}

.profile-sidebar {
    background: white;
    border-radius: 12px;
    padding: 30px;
    box-shadow: 0 2px 20px rgba(0,0,0,0.08);
    height: fit-content;
    position: sticky;
    top: 40px;
}

.profile-image {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    object-fit: cover;
    margin: 0 auto 25px;
    display: block;
    box-shadow: 0 8px 32px rgba(0,0,0,0.12);
}

.profile-name {
    font-size: 2rem;
    font-weight: 700;
    color: #2c3e50;
    margin-bottom: 8px;
    text-align: center;
}

.profile-title {
    font-size: 1rem;
    color: #7f8c8d;
    margin-bottom: 25px;
    text-align: center;
    line-height: 1.4;
}

.profile-bio {
    font-size: 0.95rem;
    color: #555;
    margin-bottom: 25px;
    line-height: 1.6;
}

.contact-links {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.contact-links a {
    color: #3498db;
    text-decoration: none;
    font-weight: 500;
    padding: 8px 0;
    transition: color 0.3s ease;
}

.contact-links a:hover {
    color: #2980b9;
}

.main-projects {
    background: white;
    border-radius: 12px;
    padding: 40px;
    box-shadow: 0 2px 20px rgba(0,0,0,0.08);
}

.section-title {
    font-size: 1.8rem;
    color: #2c3e50;
    margin-bottom: 30px;
    font-weight: 600;
}

.project {
    margin-bottom: 50px;
    padding-bottom: 40px;
    border-bottom: 1px solid #e9ecef;
}

.project:last-child {
    border-bottom: none;
    margin-bottom: 0;
}

.project-title {
    font-size: 1.4rem;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 15px;
    line-height: 1.3;
}

.project-description {
    color: #555;
    margin-bottom: 20px;
    line-height: 1.7;
    font-size: 1rem;
}

.project-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 15px;
}

.tag {
    background: #e3f2fd;
    color: #1976d2;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 500;
}

.project-link {
    color: #3498db;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.3s ease;
}

.project-link:hover {
    color: #2980b9;
}

.highlight {
    background: linear-gradient(120deg, rgba(52, 152, 219, 0.1) 0%, rgba(52, 152, 219, 0.1) 100%);
    padding: 20px;
    border-radius: 8px;
    margin: 20px 0;
    border-left: 4px solid #3498db;
}

/* Hide default Jekyll minimal theme elements that we're replacing */
header {
    display: none;
}

.wrapper h1 {
    display: none;
}

.wrapper p:first-of-type {
    display: none;
}

@media (max-width: 768px) {
    .portfolio-container {
        grid-template-columns: 1fr;
        gap: 30px;
    }
    
    .profile-sidebar {
        position: static;
        text-align: center;
    }
    
    .profile-name {
        font-size: 1.8rem;
    }
    
    .main-projects {
        padding: 25px;
    }
}
</style>

<div class="portfolio-container">
    <aside class="profile-sidebar">
        <img src="assets/profile.png" alt="Portrait of Mi-Ru Youn" class="profile-image">
        <h1 class="profile-name">Mi-Ru Youn</h1>
        <p class="profile-title">Data Science Master's Student at Boston University</p>
        <p class="profile-bio">Passionate about machine learning, statistics, and data analysis with experience in multi-agent reinforcement learning, public policy analytics, and neural networks.</p>
        <div class="contact-links">
            <a href="https://linkedin.com/in/miruayoun" target="_blank">📧 LinkedIn Profile</a>
            <a href="https://github.com/miruyoun" target="_blank">💻 View GitHub</a>
        </div>
    </aside>

    <main class="main-projects">
        <h2 class="section-title">Selected projects in machine learning, statistics, and data analysis</h2>
        
        <div class="project">
            <h3 class="project-title">Relaxed QMIX for Multi-Agent Reinforcement Learning</h3>
            <p class="project-description">
                Advanced research in multi-agent reinforcement learning focusing on improving coordination between multiple AI agents. This project explores relaxed constraints in the QMIX algorithm to enhance performance in complex multi-agent environments and cooperative tasks.
            </p>
            <div class="project-tags">
                <span class="tag">🐍 Python</span>
                <span class="tag">🤖 Reinforcement Learning</span>
                <span class="tag">🧠 Multi-Agent Systems</span>
                <span class="tag">⚡ PyTorch</span>
            </div>
            <a href="relaxedqmix" class="project-link">View project details</a>
        </div>

        <div class="project">
            <h3 class="project-title">Boston Bus Equity Analysis (GBH and BU Spark! Collaboration)</h3>
            <p class="project-description">
                Collaborative research project analyzing transportation equity in Boston's public transit system. Working with GBH and BU Spark!, this study examines bus service accessibility and equity across different neighborhoods, providing insights for policy improvements.
            </p>
            <div class="highlight">
                <strong>Impact:</strong> This research directly informs public policy decisions and contributes to improving transportation equity for Boston residents.
            </div>
            <div class="project-tags">
                <span class="tag">📊 Data Analysis</span>
                <span class="tag">🗺️ Geospatial Analysis</span>
                <span class="tag">📈 Statistics</span>
                <span class="tag">🚌 Public Policy</span>
            </div>
            <a href="mbta" class="project-link">View project details</a>
        </div>

        <div class="project">
            <h3 class="project-title">BMW Price Analysis</h3>
            <p class="project-description">
                Comprehensive analysis of BMW vehicle pricing using statistical modeling and machine learning techniques. This project explores factors affecting vehicle valuation and builds predictive models for price estimation in the automotive market.
            </p>
            <div class="project-tags">
                <span class="tag">📊 Statistical Modeling</span>
                <span class="tag">🤖 Machine Learning</span>
                <span class="tag">💰 Price Prediction</span>
                <span class="tag">📈 Regression Analysis</span>
            </div>
            <a href="bmw" class="project-link">View project details</a>
        </div>

        <div class="project">
            <h3 class="project-title">Graph Neural Networks for Dark Matter Inference</h3>
            <p class="project-description">
                Cutting-edge application of graph neural networks to astrophysics research, specifically for dark matter detection and inference. This project demonstrates the intersection of deep learning and computational physics in addressing fundamental questions about the universe.
            </p>
            <div class="project-tags">
                <span class="tag">🌌 Astrophysics</span>
                <span class="tag">🕸️ Graph Neural Networks</span>
                <span class="tag">🧠 Deep Learning</span>
                <span class="tag">🔬 Research</span>
            </div>
            <a href="darkmatter" class="project-link">View project details</a>
        </div>
    </main>
</div>