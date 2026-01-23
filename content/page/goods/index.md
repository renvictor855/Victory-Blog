---
title: "好物清单"
description: "纯粹分享我的电子个人好物~"
layout: "page"
url: "/goods/"
---

<style>
.goods-grid {
    display: grid !important;
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 20px !important;
    margin: 20px 0 !important;
}
.good-card {
    background: var(--card-background);
    border-radius: 12px;
    box-shadow: var(--shadow-l1);
    overflow: hidden;
    display: flex;
    flex-direction: column;
    border: 1px solid var(--border-color);
    text-align: center;
    transition: transform 0.3s;
}
.good-card:hover {
    transform: translateY(-5px);
}
.good-image {
    width: 100%;
    height: 160px; /* 稍微加高一点图片 */
    object-fit: cover;
    border-bottom: 1px solid var(--border-color);
}
.good-info {
    padding: 15px 10px; /* 增加内边距 */
}
.good-title {
    font-size: 1.1rem !important; /* 字体调大 */
    font-weight: bold;
    color: var(--card-text-color-main);
    margin-bottom: 8px;
}
.good-desc {
    font-size: 0.9rem !important; /* 字体调大 */
    color: var(--card-text-color-tertiary);
    line-height: 1.5;
    display: -webkit-box;
    -webkit-line-clamp: 3; /* 允许描述多显示一行，防止大字体装不下 */
    -webkit-box-orient: vertical;
    overflow: hidden;
}
@media (max-width: 640px) {
    .goods-grid {
        grid-template-columns: 1fr !important;
    }
    .good-image {
        height: 220px;
    }
}
</style>

<div class="goods-grid">
    <div class="good-card">
        <img src="https://2c.zol-img.com.cn/product/221/94/cewFU7SelE6I.jpg" class="good-image">
        <div class="good-info">
            <div class="good-title">Lenovo Xiaoxin Pro 14</div>
            <div class="good-desc">主力电脑，主要用于生产力工作和出门携带（2022.06购入）</div>
        </div>
    </div>
    <div class="good-card">
        <img src="https://2a.zol-img.com.cn/product/209/814/ceiR0uIWLL1YY.jpg" class="good-image">
        <div class="good-info">
            <div class="good-title">MacBook Air M1</div>
            <div class="good-desc">备用电脑，MacOS平台当年的尝鲜（2021.12购入）</div>
        </div>
    </div>
    <div class="good-card">
        <img src="https://2c.zol-img.com.cn/product/270/906/ceQf7gsbcNx52.jpg" class="good-image">
        <div class="good-info">
            <div class="good-title">OnePlus Ace 5</div>
            <div class="good-desc">主力手机，1TB超大存储深入我心（2025.07购入）</div>
        </div>
    </div>
    <div class="good-card">
        <img src="https://2c.zol-img.com.cn/product/225/482/ce0da5Gl4z5Dg.jpg" class="good-image">
        <div class="good-info">
            <div class="good-title">Xiaomi 13</div>
            <div class="good-desc">备用机，小屏超棒，Leica加持，摄像手机（2024.05购入）</div>
        </div>
    </div>
    <div class="good-card">
        <img src="https://2f.zol-img.com.cn/product/222_1200x900/857/ce7cUFvpyUfa6.jpg" class="good-image">
        <div class="good-info">
            <div class="good-title">iPad Air 5 (M1)</div>
            <div class="good-desc">目前当作电脑副屏使用，性能非常出色（2022.07购入）</div>
        </div>
    </div>
    <div class="good-card">
        <img src="https://www.huaweifans.com.tw/assets/images/wearables/watch-gt4/watch-gt4-color-2.png" class="good-image">
        <div class="good-info">
            <div class="good-title">Huawei Watch GT 4</div>
            <div class="good-desc">超好看的手表，用于检测健康和锻炼使用（2024.01购入）</div>
        </div>
    </div>
    <div class="good-card">
        <img src="https://2c.zol-img.com.cn/product/274/226/ceENWHfAvCF6.jpg" class="good-image">
        <div class="good-info">
            <div class="good-title">Xiaomi Buds 6</div>
            <div class="good-desc">很少带耳机，但是还是狠心买了，感知力不强（2026.01购入）</div>
        </div>
    </div>
    <div class="good-card">
        <img src="https://2e.zol-img.com.cn/product/223_1200x900/850/ce3SHuiblQImw.jpg" class="good-image">
        <div class="good-info">
            <div class="good-title">SSK 移动固态硬盘</div>
            <div class="good-desc">做了 Win To Go，存储个人重要文件（2021.06购入）</div>
        </div>
    </div>
</div>