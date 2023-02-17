def compare_histories(original_history, new_history, initial_epochs = 5):
  """
  Compares two TensorFlow History objects.
  """
  # Get Original history measurements
  acc = original_history.history['accuracy']
  loss = original_history.history['loss']

  val_acc = original_history.history['val_accuracy']
  val_loss = original_history.history['val_loss']

  # Combine origina history with new history(get history measurements after fine-tuning)
  total_acc = acc + new_history.history['accuracy']
  total_loss = loss + new_history.history['loss']

  total_val_acc = val_acc + new_history.history['val_accuracy']
  total_val_loss = val_loss + new_history.history['val_loss']

  # Make plots for accuracy
  plt.figure(figsize = (8, 8))
  plt.subplot(2, 1, 1)   # 2 rows, 1 column, 1st part (will be whaterver comes after this (in the next line of code?))
  plt.plot(total_acc, label = 'Training Accuracy')
  plt.plot(total_val_acc, label = 'Validation Accuracy')
  
  plt.plot([initial_epochs - 1, initial_epochs - 1], plt.ylim(), label = 'Start Fine Tuning')   # 
  plt.legend(loc = 'lower right')   # loc is location
  plt.title('Training and Validation Accuracy')

  # Make plots for loss 
  plt.figure(figsize = (8,  8))
  plt.subplot(2, 1, 2)
  plt.plot(total_loss, label = 'Training Loss')
  plt.plot(total_val_loss, label = 'Validation Loss')
  plt.plot([initial_epochs - 1, initial_epochs - 1], plt.ylim(), label = 'Start Fine Tuning')   
  plt.legend(loc = 'upper right')   
  plt.title('Training and Validation Loss')
