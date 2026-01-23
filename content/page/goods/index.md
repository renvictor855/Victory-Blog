---
title: "好物清单"
description: "纯粹分享我的电子个人好物~"
layout: "page"
url: "/goods/"
---

<style>
/* 强制覆盖所有主题样式，把字号拉到你满意的“大方”程度 */
.goods-grid {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 25px !important;
  margin-top: 30px !important;
}

.good-card {
  background: var(--card-background, #fff);
  border-radius: 16px;
  border: 1px solid var(--border-color, #eee);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: 0.3s;
}

.good-image {
  width: 100%;
  height: 180px;
  object-fit: contain;
  padding: 15px;
  background: #f9f9f9;
}

.good-info {
  padding: 20px !important;
  text-align: left !important; /* 左对齐通常显得更“大方” */
}

.good-title {
  font-size: 1.4rem !important; /* 这里是核心：标题大字 */
  font-weight: 800 !important;
  color: var(--card-text-color-main, #000);
  margin-bottom: 12px !important;
  display: block;
}

.good-desc {
  font-size: 1.1rem !important; /* 这里是核心：正文大字 */
  line-height: 1.6 !important;
  color: var(--card-text-color-tertiary, #666);
}

@media (max-width: 800px) {
  .goods-grid { grid-template-columns: 1fr 1fr !important; }
}
@media (max-width: 500px) {
  .goods-grid { grid-template-columns: 1fr !important; }
}
</style>

<div class="goods-grid">
  <div class="good-card">
    <img src="https://2c.zol-img.com.cn/product/221/94/cewFU7SelE6I.jpg" class="good-image">
    <div class="good-info">
      <b class="good-title">小新 Pro 14</b>
      <span class="good-desc">主力生产力电脑，性能均衡，轻便好拿。（2022.06购入）</span>
    </div>
  </div>

  <div class="good-card">
    <img src="https://2e.zol-img.com.cn/product/222/682/cecADmuIHpido.jpg" class="good-image">
    <div class="good-info">
      <b class="good-title">MacBook Air M1</b>
      <span class="good-desc">备用电脑，MacOS 独一份的流畅，当年的白月光。（2021.12购入）</span>
    </div>
  </div>

  <div class="good-card">
    <img src="https://2c.zol-img.com.cn/product/270/906/ceQf7gsbcNx52.jpg" class="good-image">
    <div class="good-info">
      <b class="good-title">一加 Ace 5</b>
      <span class="good-desc">主力手机，1TB 存储彻底告别空间焦虑。（2025.07购入）</span>
    </div>
  </div>

  <div class="good-card">
    <img src="https://2c.zol-img.com.cn/product/225/482/ce0da5Gl4z5Dg.jpg" class="good-image">
    <div class="good-info">
      <b class="good-title">小米 13</b>
      <span class="good-desc">徕卡摄影，小屏旗舰，手感真的是顶级。（2024.05购入）</span>
    </div>
  </div>

  <div class="good-card">
    <img src="https://2f.zol-img.com.cn/product/222_1200x900/857/ce7cUFvpyUfa6.jpg" class="good-image">
    <div class="good-info">
      <b class="good-title">iPad Air 5</b>
      <span class="good-desc">M1 芯片，目前作为电脑副屏提升效率。（2022.07购入）</span>
    </div>
  </div>

  <div class="good-card">
    <img src="https://2b.zol-img.com.cn/product/256/381/ceB82KHDzso4M.png" class="good-image">
    <div class="good-info">
      <b class="good-title">华为 Watch GT 4</b>
      <span class="good-desc">续航持久，健康监测，颜值担当。（2024.01购入）</span>
    </div>
  </div>

  <div class="good-card">
    <img src="https://2c.zol-img.com.cn/product/274/226/ceENWHfAvCF6.jpg" class="good-image">
    <div class="good-info">
      <b class="good-title">小米 Buds 6</b>
      <span class="good-desc">降噪出色，佩戴舒适，性价比很高。（2026.01购入）</span>
    </div>
  </div>

  <div class="good-card">
    <img src="https://2e.zol-img.com.cn/product/223_1200x900/850/ce3SHuiblQImw.jpg" class="good-image">
    <div class="good-info">
      <b class="good-title">SSK 移动硬盘</b>
      <span class="good-desc">Win To Go 随身系统，重要资料库。（2021.06购入）</span>
    </div>
  </div>
</div>