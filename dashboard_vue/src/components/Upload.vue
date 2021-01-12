<template>
 
  <input class="file-input" hidden type="file"  @change="upload($event.target.files)" />
 
   
</template>

<script lang="ts" >
import axios from "axios";
export default {
  name: "Upload",
  emits: ["file-upload"],
  setup(_ : any, context: any ) {
    const upload = async (files: FileList | null) => {
       if (files == null) return;

      const data = new FormData();
      data.append("image", files[0]);

      const res = await axios.post("upload", data);
     
      context.emit("file-upload", res.data.url);

      console.log(res);
    };

    return {
      upload,
    };
  },
};
</script>