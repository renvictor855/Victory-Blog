---
title: "好物清单"
description: "纯粹分享我的电子个人好物~"
layout: "page"
url: "/goods/"
---

<style>
/* 核心容器：增加间距，让视觉更开阔 */
.goods-grid {
    display: grid !important;
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 30px 20px !important;
    margin: 30px 0 !important;
}

/* 卡片样式：对标图1的圆角和纯白质感 */
.good-card {
    background: #ffffff;
    border-radius: 20px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    text-align: center;
    transition: all 0.3s ease;
    /* 调整边框颜色，使其更淡更高级 */
    border: 1px solid rgba(0,0,0,0.05);
}

.good-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.1);
}

/* 图片区域：保持正方形比例或稍高，背景设为浅灰防白底图消失 */
.good-image {
    width: 100%;
    height: 200px; 
    object-fit: contain; /* 改为 contain，防止产品被裁切，对标图1 */
    padding: 20px;
    background-color: #fdfdfd;
}

/* 文字区域：加大字号的关键 */
.good-info {
    padding: 10px 15px 25px 15px; 
}

/* 好物标题：对标图1的大字粗体 */
.good-title {
    font-size: 1.25rem !important; 
    font-weight: 700 !important;
    color: #1d1d1f;
    margin-bottom: 10px;
    line-height: 1.3;
}

/* 好物描述：调大字号，改用灰黑色增强易读性 */
.good-desc {
    font-size: 1.0rem !important; 
    color: #86868b;
    line-height: 1.6;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

/* 手机端适配：1行1个 */
@media (max-width: 640px) {
    .goods-grid {
        grid-template-columns: 1fr !important;
        gap: 20px !important;
    }
    .good-image {
        height: 280px;
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
            <div class="good-desc">备用电脑，MacOS平台当年的尝鲜，地流泪（2021.12购入）</div>
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
            <div class="good-desc">摄像手机，小屏超棒，Leica加持（2024.05购入）</div>
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
        <img src="https://cdn.cnbj0.fds.api.mi-img.com/b2c-shopapi-pms/pms_1736648474.3336909.jpg" class="good-image">
        <div class="good-info">
            <div class="good-title">Xiaomi Buds 6</div>
            <div class="good-desc">很少带耳机，但是还是狠心买了，感知力不强（2026.01）</div>
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