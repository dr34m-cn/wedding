<template>
	<view class="end">
		<bTitle title="记忆碎片"></bTitle>
		<view class="entAlbum" v-if="urls">
			<u-album :urls="urls" rowCount="5" :maxCount="maxCount"></u-album>
		</view>
		<view class="text" @click="maxCount = 100" v-if="maxCount == 10">展开</view>
	</view>
</template>

<script>
	import bTitle from '@/pages/components/utils/bTitle.vue';
	export default {
		name: 'end',
		components: {
			bTitle
		},
		data() {
			return {
				urls: null,
				maxCount: 10
			}
		},
		mounted() {
			this.init();
		},
		methods: {
			init() {
				this.urls = [];
				for (let i = 52; i < 63; i++) {
					this.pushIt(i);
				}
				for (let i = 1; i < 52; i++) {
					this.pushIt(i);
				}
			},
			pushIt(i) {
				let url = this.vuex_url + 'photo/';
				if (i < 10) {
					url = url + '0';
				}
				if (i < 41 || i > 55) {
					this.urls.push(url + i + '.jpg');
				} else if (i < 56) {
					this.urls.push(url + i + '.png');
				}
			}
		}
	}
</script>

<style lang="scss">
	.end {
		padding-top: 80rpx;

		.entAlbum {
			display: flex;
			align-items: center;
			justify-content: center;
		}
		
		.text {
			padding: 20rpx;
			text-align: center;
		}
	}
</style>