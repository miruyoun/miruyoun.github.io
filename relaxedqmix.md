---
layout: default
title: Relaxed QMIX
---

# Relaxed QMIX for PyMARL

Relaxed QMIX relaxes QMIX’s strict monotonicity constraint, enabling richer cooperative strategies in **StarCraft II**. This work extends the PyMARL framework with architectural modifications to allow tactical retreats and sacrificial plays that vanilla QMIX cannot capture.

---

## 🚀 Highlights
- Implemented a **correction network** with double state re-injection and L2 regularization.  
- Tuned ε to interpolate between monotonic and flexible coordination.  
- Evaluated on **SMAC benchmarks** (`8m`, `2s3z`, `MMM2`, `Corridor`).  

---

## ⚙️ Implementation
Experiments were run on **Boston University’s SCC** using NVIDIA V100 GPUs and SLURM.  
Key hyperparameters:
- ε-greedy exploration (1.0 → 0.05)  
- Replay buffer: 5000  
- Target update: every 200 episodes  
- Optimizer: RMSProp (lr = 0.0005)  

---

## 📊 Results
- **8m & 2s3z** → matched QMIX (~90% win rate).  
- **MMM2** → RelaxedQMIX reached ~70% vs QMIX’s 10%.  
- **Corridor** → remained unsolved (0%).  


- **Training Performance**  
  Relaxed QMIX achieved faster convergence than baseline QMIX on maps like *8m* and *2s3z*.  

  ![Training Curve](assets/pymarl/relaxedqmix/training_curve.png)  

- **Map Performance Comparison**  
  Relaxed QMIX significantly outperformed QMIX in heterogeneous settings like *MMM2*.  

  ![Win Rate Comparison](assets/pymarl/relaxedqmix/winrate.png)  
---

## 🎥 Video Demonstrations  

Here are two highlights showcasing the Relaxed QMIX vs QMIX training runs on StarCraft II:  

### Training Run Example  
<iframe width="560" height="315" 
        src="https://www.youtube.com/embed/_o91TFaJ-rg" 
        title="QMIX Training Run" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>
</iframe>  

### Episode Highlight  
<iframe width="560" height="315" 
        src="https://www.youtube.com/embed/To9-4rwUBhw" 
        title="Relaxed QMIX Episode Highlight" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>
</iframe>  


## 🌟 Impact
RelaxedQMIX demonstrates that **small architectural changes can significantly improve cooperative MARL performance**, especially in heterogeneous environments.

---

## 🔗 Links
- 💻 [GitHub Repository](https://github.com/miruyoun/PyMARL_RL_Project)  
- 📄 [Read Full Paper (PDF)](assets/pymarl/RelaxedQMIX_Paper.pdf)  
- 🎥 [Full Video Demos](https://www.youtube.com/playlist?list=PLfNwQXb-4EYiBC-Hm0P8xQDTPxbTGFpBp)  

---
