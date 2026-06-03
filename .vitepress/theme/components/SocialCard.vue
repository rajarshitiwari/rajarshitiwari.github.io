<template>
  <a :href="link" target="_blank" class="social-card">
    <span class="card-title">{{ title }}</span>
    <span class="card-text">
      <!-- This slot lets us pass in the text or <br> tags from the markdown -->
      <slot></slot> 
    </span>
  </a>
</template>

<script setup>
defineProps({
  title: String,
  link: String
})
</script>

<style scoped>
.social-card {
  display: flex;
  flex-direction: column;
  padding: 1.2rem;
  background-color: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  text-decoration: none !important;
  transition: all 0.25s ease;
}

.social-card:hover {
  border-color: var(--vp-c-brand);
  background-color: var(--vp-c-bg-mute);
  transform: translateY(-2px);
}

.card-title {
  font-weight: 600;
  font-size: 1.05rem;
  color: var(--vp-c-text-1);
  margin-bottom: 0.5rem;
}

.card-text {
  font-size: 0.85rem;
  color: var(--vp-c-text-2);
  line-height: 1.4;
}
</style>