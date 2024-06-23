---
layout: page
sidebar: false
---
<h1 align="center" class="fungi-title">
People of Fungi 🍄
</h1>

<script setup>
import {
  VPTeamPage,
  VPTeamPageTitle,
  VPTeamMembers,
  VPTeamPageSection
} from 'vitepress/theme'

const members = [
  {
    avatar: 'https://www.github.com/hyerland.png',
    name: 'Adam Garza',
    title: 'Creator of Fungi',
    links: [
      { icon: 'github', link: 'https://github.com/hyerland' },
      { icon: 'twitter', link: 'https://x.com/adamg_dev' }
    ]
  }
]
const partners = [
  {
    avatar: 'https://yt3.googleusercontent.com/tWrxeWzw2FvMPDrJpIBvK2jhHBKgt7Qnqhu349Qiyq3Z0i5X9xRhWsHHdErHaEhOfdOnLWeEJLk=s176-c-k-c0x00ffffff-no-rj',
    name: 'hiivemiind',
    title: 'Graphic Designer',
    links: [
      { icon: 'youtube', link: 'https://www.youtube.com/@hiivemiind.' },
    ]
  },
]
</script>

<p align="center" class="fungi-subtitle">
People of fungi (contributors, translators, etc.) are important as they shaped the project for new improvements and helped make Fungi possible. <i>In fact,
they're so important that they're all here!</i>
</p>

<br>

<p align="center">
  <img alt="Showing a mushroom guiding others to success" src="/fungi-community-1.png">
</p>

<p align="center" class="fungi-svg-animation-up-down">
  <iconify-icon icon="ep:arrow-down-bold" width="2.7rem" height="2.7rem"  style="color: #ff7bac"></iconify-icon>
</p>

<VPTeamPage>
  <VPTeamPageTitle>
    <template #title>
      Core Contributors
    </template>
    <template #lead>
      Fungi wouldn't be possible without the help of all of the people who have contributed to the project codebase.
    </template>
  </VPTeamPageTitle>
  <VPTeamMembers
    :members="members"
  />
</VPTeamPage>

<VPTeamPageSection>
    <template #title>Partners</template>
    <template #lead>Our partners in which supported the project in major ways that isn't code related.</template>
    <template #members>
      <VPTeamMembers size="small" :members="partners" />
    </template>
</VPTeamPageSection>

<br>

<p style="display: flex; justify-content: center;" class="fungi-subtitle">
Fungi wouldn't also be possible without contributions from the community on github.
</p>

<div style="display: flex; justify-content: center;">
  <a href="https://github.com/hyerland/Fungi/graphs/contributors">
    <img alt="Contributors on GitHub." src="https://contrib.rocks/image?repo=hyerland/Fungi" style="margin: auto; max-width: 100%;" />
  </a>
</div>

<div style="display: flex; align-items: center; justify-content: center;">
  <p class="fungi-paragraph" align="center">
    Thank you for contributing to Fungi! From big changes to small changes, you made fungi better than it was.
  </p>

  <p align="center" class="fungi-svg-animation-heartbeat" style="margin-bottom: 2rem;">
    <iconify-icon icon="ion:heart" width="2rem" height="2rem"  style="color: #e81111; margin: 0.1rem;"></iconify-icon>
  </p>
</div>
