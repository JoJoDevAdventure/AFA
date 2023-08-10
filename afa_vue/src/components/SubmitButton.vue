<template>
    <div>
        <!-- Button to trigger the modal -->
        <button @click="showModal()" class="bg-transparent">Submit</button>

        <!-- The modal -->
        <div class="modal" tabindex="-1" role="dialog" v-if="visible">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Modal Title</h5>
                        <button type="button" class="close" @click="hideModal">
                            <span>&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <!-- Content of the modal -->
                        <p>This is the modal content.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            visible: false
        };
    },

    methods: {
        showModal() {
            this.visible = true;
        },
        hideModal() {
            this.visible = false;
        }
    }
};
</script>

<style>

.bg-transparent {
    background-color: transparent;
    text-decoration: none;
    outline: none;
    border: none;
    color: white;
    font-size: 18px;
}

</style>