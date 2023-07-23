<template>
	<view class="pZong" :style="'width: ' + size + 'rpx;'">
		<view class="p1" :style="'width:'+size+'rpx;height:'+size+'rpx;margin-bottom:'+size+'rpx;'"></view>
		<view class="p2" :style="'width:'+size+'rpx;height:'+size+'rpx;margin-bottom:'+size+'rpx;'"></view>
		<view class="p3" :style="'width:'+size+'rpx;height:'+size+'rpx;'"></view>
	</view>
</template>

<script>
	export default {
		props: ['size'],
		name: 'pZong',
		data() {
			return {}
		},
		methods: {}
	}
</script>

<style lang="scss">
	.pZong {
		.p1 {
			background-color: #99785f;
		}
		
		.p2 {
			background-color: #7d5942;
		}
		
		.p3 {
			background-color: #311b11;
		}
	}
</style>