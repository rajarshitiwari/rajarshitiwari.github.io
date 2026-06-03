<template>
  <div class="matrix-wrapper">
    <div class="matrix-legend">
      <span class="legend-text">Familiarity:</span>
      <div class="legend-bar">
        <span class="legend-label core">Foundational</span>
        <div class="legend-gradient"></div>
        <span class="legend-label expert">Advanced Expertise</span>
      </div>
    </div>

    <div class="table-responsive">
      <table class="skills-heatmap-table">
        <tbody>
          <tr v-for="row in matrixData" :key="row.category">
            <td class="category-cell">
              {{ row.category }}
            </td>
            
            <td 
              v-for="index in 6" 
              :key="index"
              class="skill-cell"
              :style="getCellStyle(row.skills[index - 1])"
              :class="{ 'empty-cell': !row.skills[index - 1] }"
            >
              <span v-if="row.skills[index - 1]" class="skill-text">
                {{ row.skills[index - 1].name }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
// Exact data and scores from your Python script, but hidden from rendering
const matrixData = [
  {
    category: 'Language',
    skills: [
      { name: 'FORTRAN', level: 8 },
      { name: 'Python3', level: 7 },
      { name: 'Julia', level: 6 },
      { name: 'C++', level: 5 }
    ]
  },
  {
    category: 'Linux/HPC',
    skills: [
      { name: 'zsh/bash', level: 8 },
      { name: 'Linux admin', level: 8 },
      { name: 'openmp/MPI', level: 8 },
      { name: 'Cuda/GPU', level: 7 },
      { name: 'slurm', level: 7 }
    ]
  },
  {
    category: 'Machine Learning',
    skills: [
      { name: 'Tensorflow', level: 7 },
      { name: 'Pytorch', level: 6 },
      { name: 'mxnet', level: 5 },
      { name: 'scikit', level: 5 }
    ]
  },
  {
    category: 'Visualize',
    skills: [
      { name: 'Matplotlib', level: 8 },
      { name: 'Gnuplot', level: 8 },
      { name: 'asymptote', level: 8 },
      { name: 'VESTA', level: 6 }
    ]
  },
  {
    category: 'Simulation',
    skills: [
      { name: 'Monte-Carlo', level: 9 },
      { name: 'Modelling', level: 9 },
      { name: 'ase/pymatgen', level: 8 },
      { name: 'AIMS', level: 8 },
      { name: 'VASP', level: 7 },
      { name: 'qiskit', level: 5 }
    ]
  },
  {
    category: 'Tools',
    skills: [
      { name: 'MS office', level: 6 },
      { name: 'Mathematica', level: 6 },
      { name: 'emacs', level: 8 },
      { name: 'vscode', level: 6 },
      { name: 'latex', level: 8 }
    ]
  }
]

// Emulates a smooth qualitative heatmap color map (Plasma/Spectral inspired but dark/light mode friendly)
function getCellStyle(skill) {
  if (!skill) return {}
  
  // Define hue ramps based on your confidence level
  let baseColor = ''
  let textColor = '#ffffff'
  
  if (skill.level >= 9) {
    baseColor = 'rgba(112, 83, 255, 0.95)'  // Level 9: Deep Violet-Blue
  } else if (skill.level >= 8) {
    baseColor = 'rgba(142, 68, 247, 0.85)'  // Level 8: Indigo-Purple
  } else if (skill.level >= 7) {
    baseColor = 'rgba(190, 51, 237, 0.8)'   // Level 7: Vibrant Magenta
  } else if (skill.level >= 6) {
    baseColor = 'rgba(224, 51, 201, 0.75)'  // Level 6: Soft Orchid
  } else {
    baseColor = 'rgba(240, 80, 150, 0.65)'  // Level 5: Foundational Rose
  }

  return {
    backgroundColor: baseColor,
    color: textColor
  }
}
</script>

<style scoped>
.matrix-wrapper {
  margin: 1.5rem 0;
  width: 100%;
}

.matrix-legend {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
  font-size: 0.85rem;
}

.legend-text {
  font-weight: 600;
  color: var(--vp-c-text-2);
}

.legend-bar {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  width: 100%;
  max-width: 320px;
}

.legend-label {
  font-size: 0.75rem;
  color: var(--vp-c-text-3);
}

.legend-gradient {
  flex-grow: 1;
  height: 8px;
  border-radius: 4px;
  background: linear-gradient(to right, rgba(240, 80, 150, 0.65), rgba(112, 83, 255, 0.95));
}

.table-responsive {
  width: 100%;
  overflow-x: auto;
  border-radius: 6px;
  border: 1px solid var(--vp-c-divider);
}

.skills-heatmap-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
  margin: 0;
  table-layout: fixed;
}

.skills-heatmap-table tr {
  border-bottom: 1px solid var(--vp-c-divider);
}

.skills-heatmap-table tr:last-child {
  border-bottom: none;
}

.category-cell {
  font-weight: bold;
  background: var(--vp-c-bg-mute);
  color: var(--vp-c-text-1);
  padding: 10px 12px;
  width: 140px;
  text-align: left;
  border-right: 1px solid var(--vp-c-divider);
}

.skill-cell {
  padding: 10px 8px;
  text-align: center;
  font-weight: 500;
  transition: opacity 0.2s ease;
}

.skill-cell:not(.empty-cell):hover {
  filter: brightness(1.1);
  cursor: default;
}

.empty-cell {
  background: var(--vp-c-bg-soft);
  opacity: 0.25;
}

.skill-text {
  display: inline-block;
  word-break: break-word;
  line-height: 1.2;
}

/* Ensure formatting adapts cleanly on narrow displays */
@media (max-width: 768px) {
  .skills-heatmap-table {
    width: 650px; /* Forces scroll container rather than squishing layout */
  }
}
</style>