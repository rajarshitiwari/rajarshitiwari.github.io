<template>
  <div class="home-profile-container">
    <!-- Hero Section -->
    <div class="hero-section" v-if="frontmatter.hero">
      <h1 class="hero-name">{{ frontmatter.hero.name }}</h1>
      <p class="hero-text">{{ frontmatter.hero.text }}</p>
      <p class="hero-tagline">{{ frontmatter.hero.tagline }}</p>
      
      <div class="hero-actions" v-if="frontmatter.hero.actions">
        <a 
          v-for="(action, index) in frontmatter.hero.actions" 
          :key="index"
          :href="action.link" 
          :class="['action-btn', action.theme]"
        >
          {{ action.text }}
        </a>
      </div>
    </div>

    <!-- Features Grid -->
    <div class="features-grid" v-if="frontmatter.features">
      <div 
        v-for="(feature, index) in frontmatter.features" 
        :key="index" 
        class="feature-card"
      >
        <h3 class="feature-title">{{ feature.title }}</h3>
        <p class="feature-details">{{ feature.details }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useData } from 'vitepress'

// This pulls the YAML block directly from the markdown file this component sits in!
const { frontmatter } = useData()
</script>

<style scoped>
/* Keep all the exact same CSS from the previous step here */
.home-profile-container { margin-top: 2rem; }

.hero-section { text-align: center; padding: 3rem 0; }
.hero-name {
  font-size: 3rem;
  font-weight: 800;
  background: -webkit-linear-gradient(120deg, var(--vp-c-brand-1) 30%, var(--vp-c-brand-next));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 0.5rem;
  line-height: 1.2;
}
.hero-text { font-size: 2rem; font-weight: 700; color: var(--vp-c-text-1); margin-bottom: 1rem; line-height: 1.2; }
.hero-tagline { font-size: 1.2rem; color: var(--vp-c-text-2); margin-bottom: 2rem; }

.hero-actions { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
.action-btn { display: inline-block; padding: 0.75rem 1.5rem; border-radius: 20px; font-weight: 600; text-decoration: none !important; transition: all 0.2s ease; }
.action-btn.brand { background-color: var(--vp-c-brand-1); color: white; }
.action-btn.brand:hover { background-color: var(--vp-c-brand-2); }
.action-btn.alt { background-color: var(--vp-c-bg-mute); color: var(--vp-c-text-1); }
.action-btn.alt:hover { background-color: var(--vp-c-bg-soft); }

.features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin-top: 2rem; padding-top: 2rem; border-top: 1px solid var(--vp-c-divider); }
.feature-card { background: var(--vp-c-bg-soft); padding: 1.5rem; border-radius: 12px; border: 1px solid var(--vp-c-divider); }
.feature-title { font-size: 1.1rem; font-weight: 600; margin-bottom: 0.75rem; color: var(--vp-c-text-1); }
.feature-details { font-size: 0.95rem; color: var(--vp-c-text-2); line-height: 1.5; }
</style>