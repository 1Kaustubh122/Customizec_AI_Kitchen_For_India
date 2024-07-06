def photo_pred():
    import os
    import numpy as np
    import pandas as pd
    from tensorflow.keras.models import load_model
    from tensorflow.keras.preprocessing import image
    from tensorflow.keras.applications.vgg16 import preprocess_input
    import tensorflow as tf


    from tensorflow.keras.models import load_model
    model = load_model('food_classification_model.keras')

    def preprocess_image(img_path, target_size=(224, 224)):
        """Preprocess the image for model prediction."""
        img = image.load_img(img_path, target_size=target_size)
        img_array = image.img_to_array(img)
        img_array = preprocess_input(img_array)
        img_array = tf.expand_dims(img_array, 0)  # Create batch dimension
        return img_array

    def predict_image(img_path, model):
        """Predict the class of an image using the model."""
        img_array = preprocess_image(img_path)
        predictions = model.predict(img_array)
        class_index = np.argmax(predictions, axis=1)[0]
        return class_index

    def test_all_images(data_dir, model):
        """Test all images in the specified directory."""
        results = []
        class_labels = ['bhindi_masala', 'biryani', 'lassi', 'litti_chokha', 'misi_roti','mysore_pak']
        
        for root, dirs, files in os.walk(data_dir):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    img_path = os.path.join(root, file)
                    true_class = os.path.basename(root)
                    predicted_class_index = predict_image(img_path, model)
                    predicted_class_label = class_labels[predicted_class_index]
                    
                    # results.append({
                    #     'Image Path': img_path,
                    #     'True Class': true_class,
                    #     'Predicted Class': predicted_class_label
                    # })
        
        # return pd.DataFrame(results)
        return predicted_class_label

    # Example usage
    data_dir = '/Users/kaustubhkrishna/Documents/INTEL_UNNATI/uploads'
    results_df = test_all_images(data_dir, model)

    import os
    import shutil

    def clear_folder(folder_path):
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            os.makedirs(folder_path)
        else:
            print(f"The folder {folder_path} does not exist.")


    folder_path = '/Users/kaustubhkrishna/Documents/INTEL_UNNATI/uploads'

    clear_folder(folder_path)
    print(f"results_df = {results_df}")
    return (results_df)
