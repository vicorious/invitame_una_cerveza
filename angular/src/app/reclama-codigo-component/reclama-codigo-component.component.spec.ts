import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ReclamaCodigoComponentComponent } from './reclama-codigo-component.component';

describe('ReclamaCodigoComponentComponent', () => {
  let component: ReclamaCodigoComponentComponent;
  let fixture: ComponentFixture<ReclamaCodigoComponentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ReclamaCodigoComponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ReclamaCodigoComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
