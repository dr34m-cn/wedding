<template>
	<view class="bTitle">
		<view class="left line"></view>
		<view class="title">{{title}}</view>
		<view class="right line"></view>
	</view>
</template>

<script>
	export default {
		props: ['title'],
		name: 'bTitle',
		data() {
			return {}
		},
		methods: {}
	}
</script>

<style lang="scss">
	.bTitle {
		display: flex;
		align-items: center;
		justify-content: center;
		margin-top: 80rpx;
		margin-bottom: 40rpx;
		.line {
			width: 30rpx;
			height: 26rpx;
		}
		
		.left {
			border-top: 4rpx solid #7a5138;
			border-left: 4rpx solid #7a5138;
			margin-bottom: 60rpx;
			margin-right: -10rpx;
		}
		
		.title {
			color: #e6bca3;
			padding: 4rpx 35rpx;
			background-color: rgb(122, 81, 56);
			font-size: 28rpx;
		}
		
		.right {
			border-bottom: 4rpx solid #7a5138;
			border-right: 4rpx solid #7a5138;
			margin-top: 60rpx;
			margin-left: -10rpx;
		}
	}
</style>