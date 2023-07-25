<template>
	<view :style="'width: '+size*5+'rpx;padding-top:'+top+'rpx;margin-left:'+margin+'rpx;'">
		<view class="pHeng">
			<view class="p1" :style="'width:'+size+'rpx;height:'+size+'rpx;'"></view>
			<view class="p2" :style="'width:'+size+'rpx;height:'+size+'rpx;margin-left:'+size+'rpx;'"></view>
			<view class="p3" :style="'width:'+size+'rpx;height:'+size+'rpx;margin-left:'+size+'rpx;'"></view>
		</view>
	</view>
</template>

<script>
	export default {
		props: ['size','top','margin'],
		name: 'pHeng',
		data() {
			return {}
		},
		methods: {}
	}
</script>

<style lang="scss">
	.pHeng {
		display: flex;
		align-items: center;
		justify-content: center;

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