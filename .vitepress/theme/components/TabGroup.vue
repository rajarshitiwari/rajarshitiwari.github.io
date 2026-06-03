<template>
  <div class="tab-group-container">
    <div class="tab-headers">
      <button 
        v-for="(label, index) in labels" 
        :key="index"
        class="tab-button"
        :class="{ active: activeIndex === index }"
        @click="activeIndex = index"
      >
        {{ label }}
      </button>
    </div>
    <div class="tab-content">
      <!-- Dynamically renders the selected slot based on the active index -->
      <slot :name="`tab-${activeIndex}`"></slot>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
  labels: {
    type: Array,
    required: true
  }
})

const activeIndex = ref(0)
</script>

<style scoped>
.tab-group-container {
  margin: 1.5rem 0;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  overflow: hidden;
  background: var(--vp-c-bg-soft);
}

.tab-headers {
  display: flex;
  border-bottom: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-mute);
  overflow-x: auto;
}

.tab-button {
  padding: 0.75rem 1.5rem;
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--vp-c-text-2);
  background: transparent;
  border: none;
  border-bottom: 2px solid transparent;
  cursor: pointer;
  transition: all 0.2s ease;
  white-space: nowrap;
}

.tab-button:hover {
  color: var(--vp-c-text-1);
}

.tab-button.active {
  color: var(--vp-brand-1, var(--vp-c-brand));
  border-bottom-color: var(--vp-brand-1, var(--vp-c-brand));
  background: var(--vp-c-bg-soft);
}

.tab-content {
  padding: 1.5rem;
}

/* Add this to the bottom of the style block in TabGroup.vue */

/* Force slotted Markdown tables to take full width */
.tab-content :deep(table) {
  width: 100%;
  display: table; /* Overrides VitePress's default block display */
  margin: 0;
}

/* Keep the first column (the emoji icons) perfectly narrow */
.tab-content :deep(th:first-child),
.tab-content :deep(td:first-child) {
  width: 50px;
  text-align: center;
  border-right: 1px solid var(--vp-c-divider); /* Optional: adds a neat dividing line */
}

/* Remove default table striping/hover if it conflicts with the tab background */
.tab-content :deep(tr:nth-child(2n)) {
  background-color: transparent;
}
</style>