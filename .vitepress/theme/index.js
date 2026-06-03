import DefaultTheme from 'vitepress/theme'
import SkillsMatrix from './components/SkillsMatrix.vue'
import SocialGrid from './components/SocialGrid.vue'
import SocialCard from './components/SocialCard.vue'
import CvHeader from './components/CvHeader.vue'
import TabGroup from './components/TabGroup.vue'
import HomeProfile from './components/HomeProfile.vue'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('SkillsMatrix', SkillsMatrix)
    app.component('SocialGrid', SocialGrid)
    app.component('SocialCard', SocialCard)
    app.component('CvHeader', CvHeader)
    app.component('TabGroup', TabGroup)
    app.component('HomeProfile', HomeProfile)
  }
}
