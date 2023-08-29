namespace WindowsEx000
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            btn = new Button();
            lblMsg = new Label();
            SuspendLayout();
            // 
            // btn
            // 
            btn.Cursor = Cursors.Hand;
            btn.Font = new Font("Segoe UI", 20.25F, FontStyle.Bold, GraphicsUnit.Point);
            btn.Location = new Point(221, 152);
            btn.Name = "btn";
            btn.Size = new Size(163, 76);
            btn.TabIndex = 0;
            btn.Text = "Click here!";
            btn.UseVisualStyleBackColor = true;
            btn.Click += btn_Click;
            // 
            // lblMsg
            // 
            lblMsg.Font = new Font("Segoe UI Semibold", 15.75F, FontStyle.Bold | FontStyle.Italic, GraphicsUnit.Point);
            lblMsg.Location = new Point(231, 34);
            lblMsg.Name = "lblMsg";
            lblMsg.Size = new Size(137, 52);
            lblMsg.TabIndex = 1;
            lblMsg.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(580, 379);
            Controls.Add(lblMsg);
            Controls.Add(btn);
            MinimizeBox = false;
            Name = "Form1";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "First C# Program";
            Load += Form1_Load;
            ResumeLayout(false);
        }

        #endregion

        private Button btn;
        private Label lblMsg;
    }
}